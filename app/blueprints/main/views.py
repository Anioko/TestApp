from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_required
from sqlalchemy import desc, func
from app.email import send_email
from .forms import *

main = Blueprint('main', __name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/home')
@login_required
def index():
    check_org_exist = db.session.query(Organisation).filter_by(user_id=current_user.id).first()
    return render_template('main/user_dashboard.html', check_org_exist=check_org_exist)


@main.route('/feed')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('public.index'))
    ''' this is where users will see their feeds'''
    return render_template('main/user_feed.html')


@main.route('/profile', methods=['GET', 'POST'])
def profile():
    return redirect(url_for('account.profile'))


@main.route('/list/', defaults={'page': 1})
@main.route('/list/page/<int:page>', methods=['GET'])
@login_required
def select_section(page):
    paginated = User.query.filter(User.id != current_user.id).order_by(User.id.desc()).paginate(page, per_page=25)
    return render_template('main/selection.html', paginated=paginated)


@main.route('/profile/<int:user_id>/', methods=['GET'], defaults={'active': 'posts', 'page': 1})
@main.route('/profile/<int:user_id>/<active>', methods=['GET'], defaults={'page': 1})
@main.route('/profile/<int:user_id>/<active>/page/<page>', methods=['GET'])
def user_detail(user_id, active, page):
    """Provide HTML page with all details on a given user """
    user = User.query.get_or_404(user_id)
    if active == 'posts':
        items = user.posts.paginate(page, per_page=10)
    elif active == 'questions':
        items = user.questions.paginate(page, per_page=10)
    else:
        items = []
    user_id = Photo.user_id
    photo = Photo.query.filter_by(id=user_id).limit(1).all()
    return render_template('public/profile.html', user=user, current_user=current_user, photo=photo, id=User.id,
                           items=items)


@main.route('/user/<int:id>/<full_name>', defaults={'active': 'posts', 'page': 1})
@main.route('/user/<int:id>/<full_name>/<active>', defaults={'page': 1})
@main.route('/user/<int:id>/<full_name>/<active>/page/<int:page>')
@login_required
def user(id, full_name, active, page):
    user = db.session.query(User).filter(User.id == id, User.full_name == full_name).first()
    edit_form = PostForm()
    if user == current_user:
        return redirect(url_for('main.profile', active=active))
    if active == 'posts':
        items = user.posts.paginate(page, per_page=10)
    elif active == 'questions':
        items = user.questions.paginate(page, per_page=10)
    else:
        items = []
    return render_template('main/profile.html', user=user, active=active, items=items,
                           edit_form=edit_form)  # , photo=photo)


@main.route('/<int:id>/follow/<full_name>')
@login_required
def follow(id, full_name):
    user = db.session.query(User).filter(User.id == id, User.full_name == full_name).first()
    if user is None:
        flash('User {} not found.'.format(full_name))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('main.user', id=id, full_name=full_name))
    current_user.follow(user)
    db.session.commit()
    n = user.add_notification('new_follower', {"count": current_user.new_followers() + 1}, related_id=current_user.id,
                          permanent=True)
    flash('You are following {}!'.format(full_name))
    return redirect(url_for('main.user', id=id, full_name=full_name))


@main.route('/<int:id>/unfollow/<full_name>')
@login_required
def unfollow(id, full_name):
    user = db.session.query(User).filter(User.id == id, User.full_name == full_name).first()
    if user is None:
        flash('User {} not found.'.format(full_name))
        return redirect(url_for(main.index))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('main.user', id=id, full_name=full_name))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}!'.format(full_name))
    return redirect(url_for('main.user', id=id, full_name=full_name))


@main.route("/<user_id>/followers", methods=['GET'], defaults={'page': 1})
@main.route("/<user_id>/followers/<int:page>", methods=['GET'])
@login_required
def followers(user_id, page):
    user_instance = User.query.get(user_id)
    if user_instance == current_user:
        title = "My Followers"
    else:
        title = "{} Followers".format(user_instance.full_name)
    followers_users = user_instance.followers.paginate(page, per_page=10)
    return render_template('main/selection.html', paginated=followers_users, user_id=user_id, title=title)


@main.route("/<user_id>/following", methods=['GET'], defaults={'page': 1})
@main.route('/<user_id>/following/<int:page>', methods=['GET'])
@login_required
def following(user_id, page):
    user_instance = User.query.get(user_id)
    if user_instance == current_user:
        title = "My Followings"
    else:
        title = "{} Followings".format(user_instance.full_name)
    following_users = user_instance.followed.paginate(page, per_page=10)
    return render_template('main/selection.html', paginated=following_users, user_id=user_id, title=title)


@main.route('/photo/upload', methods=['GET', 'POST'])
@login_required
def photo_upload():
    ''' check if photo already exist, if it does, send to homepage. Avoid duplicate upload here'''
    check_photo_exist = db.session.query(Photo).filter(Photo.user_id == current_user.id).count()
    if check_photo_exist >= 1:
        pass
        # return redirect(url_for('main.index'))
    form = PhotoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            image_filename = images.save(request.files['photo'])
            image_url = images.url(image_filename)
            picture_photo = Photo.query.filter_by(user_id=current_user.id).first()
            if not picture_photo:
                picture_photo = Photo(
                    image_filename=image_filename,
                    image_url=image_url,
                    user_id=current_user.id,
                )
            else:
                picture_photo.image_filename = image_filename
                picture_photo.image_url = image_url
            db.session.add(picture_photo)
            db.session.commit()
            flash("Image saved.")
            return redirect(url_for('main.index'))
        else:
            flash('ERROR! Photo was not saved.', 'error')
    return render_template('main/upload.html', form=form)


@main.route('/invite-colleague', methods=['GET', 'POST'])
@login_required
def invite_user():
    """Invites a new user to create an account and set their own password."""

    form = InviteUserForm()
    if form.validate_on_submit():
        invited_by = db.session.query(User).filter_by(id=current_user.id).first()
        user = User(
            invited_by=invited_by.full_name,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        invite_link = url_for(
            'account.join_from_invite',
            user_id=user.id,
            token=token,
            _external=True)

        get_queue().enqueue(
            send_email,
            recipient=user.email,
            subject='You Are Invited To Join',
            template='account/email/invite',
            user=user,
            invited_by=invited_by,
            invite_link=invite_link,
            invite_by=invited_by
        )
        flash('User {} successfully invited'.format(user.full_name),
              'form-success')
        return redirect(url_for('main.index'))
    return render_template('main/new_user.html', form=form)


@main.route('/conversation/<recipient>/<full_name>', methods=['GET', 'POST'])
@login_required
def send_message(recipient, full_name):
    user = User.query.filter(User.id != current_user.id).filter_by(id=recipient).first_or_404()
    for message in current_user.history(user.id):
        if message.recipient_id == current_user.id:
            message.read_at = db.func.now()
        db.session.add(message)
    db.session.commit()
    form = MessageForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            msg = Message(user_id=current_user.id, recipient=user,
                          body=form.message.data)
            db.session.add(msg)
            db.session.commit()
            user.add_notification('unread_message', {'message': msg.id, 'count': user.new_messages()},
                                  related_id=current_user.id, permanent=True)
            flash('Your message has been sent.')
            return redirect(url_for('main.send_message', recipient=user.id, full_name=user.full_name))
    follow_lists = User.query.filter(User.id != current_user.id).order_by(func.random()).limit(10).all()
    jobs = Job.query.filter(Job.organisation != None).filter(Job.end_date >= datetime.now()).order_by(
        Job.pub_date.asc()).all()
    return render_template('main/send_messages.html', title='Send Message',
                           form=form, recipient=user, current_user=current_user, follow_lists=follow_lists, jobs=jobs)


@main.route('/conversations', defaults={'page': 1}, methods=['GET'])
@main.route('/conversations/<page>', methods=['GET'])
@login_required
def conversations(page):
    current_user.last_message_read_time = datetime.utcnow()
    db.session.commit()
    messages = current_user.messages_received.order_by(
        Message.timestamp.desc()).paginate(
        page, 10, False)
    conversations = Message.query.filter(
        or_(Message.user_id == current_user.id, Message.recipient_id == current_user.id)).all()
    user_ids = [conversation.user_id for conversation in conversations] + [conversation.recipient_id for conversation in
                                                                           conversations]
    user_ids = list(set(user_ids))
    if current_user.id in user_ids:
        user_ids.remove(current_user.id)
    users = User.query.filter(User.id.in_(user_ids)).paginate(page, per_page=20)
    follow_lists = User.query.filter(User.id != current_user.id).order_by(func.random()).limit(10).all()
    jobs = Job.query.filter(Job.organisation != None).filter(Job.end_date >= datetime.now()).order_by(
        Job.pub_date.asc()).all()
    return render_template('main/messages.html', messages=messages.items, users=users, follow_lists=follow_lists,
                           jobs=jobs)


@main.route('/question/<question_id>/edit', methods=['POST'])
@login_required
def edit_question(question_id):
    question = Question.query.filter_by(user_id=current_user.id).filter_by(id=question_id).first_or_404()
    form = QuestionForm()
    if form.validate_on_submit():
        question.title = form.title.data
        question.description = form.description.data
        db.session.add(question)
        db.session.commit()
        flash("Edited.", 'success')

        return redirect(url_for('main.question'))
    else:
        flash('ERROR! Question was not edited.', 'error')


@main.route('/question/<question_id>/delete', methods=['POST'])
def delete_question(question_id):
    question = Question.query.filter_by(user_id=current_user.id).filter_by(id=question_id).first_or_404()
    db.session.delete(question)
    db.session.commit()
    flash("Delete.", 'success')
    return redirect(url_for('main.question'))


@main.route('/questions', methods=['GET', 'POST'])
@login_required
def question():
    form = QuestionForm()
    edit_form = QuestionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            author = db.session.query(User).filter_by(id=current_user.id).first()
            posts = Question(
                title=form.title.data,
                description=form.description.data,
                user_id=current_user.id,
                author=author.full_name,
                level=1
            )
            db.session.add(posts)
            db.session.commit()
            flash("Posted.", 'success')

            return redirect(url_for('main.question'))
        else:
            flash('ERROR! Question was not created.', 'error')
    follow_lists = User.query.filter(User.id != current_user.id).order_by(func.random()).limit(10).all()
    jobs = Job.query.filter(Job.organisation != None).filter(Job.end_date >= datetime.now()).order_by(
        Job.pub_date.asc()).all()
    users = User.query.filter(Question.user_id == User.id).first()
    questions = Question.query.filter(Question.user_id != None).order_by(desc(Question.timestamp)).all()
    return render_template('main/create_question.html', form=form,
                           follow_lists=follow_lists, users=users, results=questions, jobs=jobs, edit_form=edit_form)


@main.route('/questions/list/all')
def questions_list():
    appts = Question.query.filter(Question.timestamp != None).all()
    return render_template('main/allquestions.html', appts=appts)


@main.route('/question/<int:question_id>/<title>/')
def question_details(question_id, title):
    """Provide HTML page with all details on a given question.
    """
    # Query: get Position object by ID.
    post = Question.query.filter(Question.title == title).first()
    edit_form = QuestionForm()
    return render_template('main/question_details.html', post=post, edit_form=edit_form)


@main.route('/question/answer/<answer_id>/edit', methods=['POST'])
@login_required
def edit_answer(answer_id):
    answer = Answer.query.filter_by(user_id=current_user.id).filter_by(id=answer_id).first_or_404()
    question = answer.question
    body = request.form['reply']
    answer.body = body
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('main.question_details', question_id=question.id, title=question.title))


@main.route('/question/answer/<answer_id>/delete', methods=['POST'])
def delete_answer(answer_id):
    answer = Answer.query.filter_by(user_id=current_user.id).filter_by(id=answer_id).first_or_404()
    question = answer.question
    db.session.delete(answer)
    db.session.commit()
    flash("Deleted Successfully.", 'success')
    return redirect(url_for('main.question_details', question_id=question.id, title=question.title))


@main.route('/question/answer', methods=['GET', 'POST'])
@login_required
def parent_answers():
    if request.method == 'POST':
        body = request.form['reply']
        question = Question.query.filter_by(id=request.form['question_id']).first()
        photo = current_user.photos.first()
        answers = Answer(user_id=current_user.id,
                         author=current_user.full_name,
                         question_id=question.id,
                         body=body,
                         )
        if request.form['parent_id'] != '0':
            answers.parent_id = request.form['parent_id']
        if photo:
            answers.image_url = photo.image_url
        db.session.add(answers)
        db.session.commit()
        if current_user != question.user:
            question.user.add_notification('answer', {'count': len(question.answers.all()), 'question': question.id,
                                                      'answer': answers.id}, related_id=current_user.id, permanent=True)
        return redirect(url_for('main.question_details', question_id=question.id, title=question.title))
    return render_template('main/create_question.html')


@main.route('/notification/read/<notification_id>')
@login_required
def read_notification(notification_id):
    notification = current_user.notifications.filter_by(id=notification_id).first_or_404()
    notification.read = True
    db.session.add(notification)
    db.session.commit()
    if 'unread_message' in notification.name:
        user = User.query.filter_by(id=notification.related_id).first_or_404()
        link = url_for('main.send_message', recipient=user.id, full_name=user.full_name)
    elif 'post_likes' in notification.name:
        user = User.query.filter_by(id=notification.related_id).first_or_404()
        post = Post.query.filter_by(id=json.loads(notification.payload_json)['post']).first_or_404()
        link = url_for('post.view_post', post_id=post.id)
    elif 'post_replies' in notification.name:
        user = User.query.filter_by(id=notification.related_id).first_or_404()
        post = Post.query.filter_by(id=json.loads(notification.payload_json)['post']).first_or_404()
        link = url_for('post.view_post', post_id=post.id)
    elif 'answer' in notification.name:
        user = User.query.filter_by(id=notification.related_id).first_or_404()
        question = Question.query.filter_by(id=json.loads(notification.payload_json)['question']).first_or_404()
        link = url_for('main.question_details', question_id=question.id, title=question.title)
    elif 'new_follower' in notification.name:
        user = User.query.filter_by(id=notification.related_id).first_or_404()
        link = url_for('main.user', id=user.id, full_name=user.full_name)
    elif 'new_post_of_followers' in notification.name:
        post = Post.query.filter_by(id=json.loads(notification.payload_json)['post']).first()
        link = url_for('post.view_post', post_id=post.id)
    elif 'new_job' in notification.name:
        job = Job.query.filter_by(id=json.loads(notification.payload_json)['job']).first()
        link = url_for('jobs.job_details', position_id=job.id, position_title=job.position_title,
                       position_city=job.position_city, position_state=job.position_state,
                       position_country=job.position_country)

    return redirect(link)


@main.route('/notifications/count')
@login_required
def notifications_count():
    notifications = Notification.query.filter_by(read=False).filter_by(user_id=current_user.id).count()
    messages = current_user.new_messages()

    return jsonify({
        'status': 1,
        'notifications': notifications,
        'messages': messages
    })


@main.route('/notifications')
@login_required
def notifications():
    follow_lists = User.query.filter(User.id != current_user.id).order_by(func.random()).limit(10).all()
    jobs = Job.query.filter(Job.organisation != None).filter(Job.end_date >= datetime.now()).order_by(
        Job.pub_date.asc()).all()
    users = User.query.order_by(User.full_name).all()
    notifications = current_user.notifications.all()
    parsed_notifications = []
    for notification in notifications:
        parsed_notifications.append(notification.parsed())
    parsed_notifications = sorted(parsed_notifications, key=lambda i: i['time'])
    parsed_notifications.reverse()
    parsed_notifications = parsed_notifications[0:15]
    return render_template('main/notifications.html', follow_lists=follow_lists, users=users, jobs=jobs,
                           notifications=parsed_notifications)


@main.route('/notifications/more/<int:count>')
@login_required
def more_notifications(count):
    # follow_lists = User.query.filter(User.id != current_user.id).order_by(func.random()).limit(10).all()
    # jobs = Job.query.filter(Job.organisation != None).filter(Job.end_date >= datetime.now()).order_by(Job.pub_date.asc()).all()
    # users = User.query.order_by(User.full_name).all()
    notifications = current_user.notifications.all()
    print(len(notifications))
    parsed_notifications = []
    for notification in notifications:
        parsed_notifications.append(notification.parsed())
    parsed_notifications = sorted(parsed_notifications, key=lambda i: i['time'])
    parsed_notifications.reverse()
    if count == 0:
        parsed_notifications = parsed_notifications[0:15]
    elif count >= len(parsed_notifications):
        return "<br><br><h2>No more Notifications</h2>"
    else:
        parsed_notifications = parsed_notifications[count:count + 15]
    return render_template('main/more_notifications.html', notifications=parsed_notifications)


@main.route('/notification_test')
@login_required
def notification_test():
    n = Notification.query.get(379)
    related = User.query.get(32)
    extra = Job.query.get(17)
    extraextra = Answer.query.get(25)
    return render_template('account/email/notification.html', user=current_user, link="http://www.google.com",
                           notification=n, related=related, extra=extra,
                           extraextra=extraextra)
