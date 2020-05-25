from flask import Blueprint, render_template, abort, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_required

from app.models import *

professionals = Blueprint('professionals', __name__)


@professionals.route('/list/')
def professionals_list():
    #appts = Professionals.query.filter(Professionals.organisation != None).filter(Professionals.end_date >= datetime.now()).order_by(Professionals.pub_date.asc()).all()
    #return render_template('professionals/allprofessionals.html', appts=appts)
    #def professionals_list():
    appts = Professionals.query.filter(Professionals.organisation != None).filter(Professionals.end_date >= datetime.now()).order_by(Professionals.pub_date.asc()).all()
    return render_template('professionals/allprofessionals.html', appts=appts)




@professionals.route('/<int:professionals_id>/<professionals_title>/<professionals_city>/<professionals_state>/<professionals_country>')
def professionals_details(professionals_id, professionals_title, professionals_city, professionals_state, professionals_country):
    appts = Professionals.query.filter(Professionals.id == professionals_id).first_or_404()
    org_users = User.query.all()
    orgs = Organisation.query.filter(Organisation.user_id == User.id).all()
    return render_template('professionals/professionals_details.html', appt=appts, orgs=orgs, org_users=org_users)


@professionals.route('/<int:professionals_id>/<professionals_title>/apply')
@login_required
def professionals_apply(professionals_id, professionals_title):
    appt = db.session.query(Professionals).get(professionals_id)
    if appt is None:
        abort(404)
    elif current_user.id is None:
        abort(403)
    
    else:
        
        if appt.creator == current_user:
            flash("You can't apply to {0} because you created it".format(appt.professionals_title), 'warning')
            return redirect(url_for('professionals.professionals_list'))
        extra = Extra.query.filter_by(user_id=current_user.id).first()
        if not extra:
            flash(
                "You can't participate to {0} because you didn't add your extra details , please go to <a href='{1}'>profile</a> to add it".format(
                    appt.professionals_title, url_for('account.change_extra_details')), 'warning')
            return redirect(url_for('professionals.professionals_list'))
        submissions = Submission.query.filter(Submission.professionals_id == appt.id).all()
        submissions = [appt.user_id for appt in submissions]
        if current_user.id in submissions:
            flash("You have <strong>already participated</strong> for {0}.".format(appt.professionals_title), 'warning')
            return redirect(url_for('professionals.professionals_list'))
        else:
            appts = Submission(professionals_id=appt.id, user_id=current_user.id)
            db.session.add(appts)
            db.session.commit()
            flash("You have successfully participated to {0}.".format(appt.professionals_title), 'success')
            return redirect(url_for('professionals.professionals_list'))


@professionals.route('/some-endpoint', methods=['POST'])
def share_email():
    share_text = "Your friend {0} on http://teachera.org want to recommend you this open course: {1}.\n" \
                 "Register, and view it here: {2}." \
                 "\n\n" \
                 "Regards,\n" \
                 "Teachera.org team"

    formated_text = share_text.format(current_user.name, request.form['title'], request.form['url'])
    message = Message(subject="#Write Something Here!",
                      sender='#Write Something Here!',
                      reply_to=current_user.email,
                      recipients=[request.form['email']],
                      body=formated_text)
    mail.send(message)

    print(request.__dict__)
    print(request.form)
    return jsonify(status='success')
