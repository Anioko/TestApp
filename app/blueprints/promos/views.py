from flask import Blueprint, render_template, abort, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_required

from app.models import *

promos = Blueprint('promos', __name__)


@promos.route('/list/')
def promos_list():
    #appts = Promo.query.filter(Promo.organisation != None).filter(Promo.end_date >= datetime.now()).order_by(Promo.pub_date.asc()).all()
    #return render_template('promos/allprofessionals.html', appts=appts)
    #def promos_list():
    appts = Promo.query.filter(Promo.organisation != None).filter(Promo.end_date >= datetime.now()).order_by(Promo.pub_date.asc()).all()
    return render_template('promos/allprofessionals.html', appts=appts)




@promos.route('/<int:promo_id>/<promo_title>/<promo_city>/<promo_state>/<promo_country>')
def promo_details(promo_id, promo_title, promo_city, promo_state, promo_country):
    appts = Promo.query.filter(Promo.id == promo_id).first_or_404()
    org_users = User.query.all()
    orgs = Organisation.query.filter(Organisation.user_id == User.id).all()
    return render_template('promos/professionals_details.html', appt=appts, orgs=orgs, org_users=org_users)


@promos.route('/<int:promo_id>/<promo_title>/apply')
@login_required
def promo_apply(promo_id, promo_title):
    appt = db.session.query(Promo).get(promo_id)
    if appt is None:
        abort(404)
    elif current_user.id is None:
        abort(403)
    
    else:
        
        if appt.creator == current_user:
            flash("You can't apply to {0} because you created it".format(appt.promo_title), 'warning')
            return redirect(url_for('promos.promos_list'))
        extra = Extra.query.filter_by(user_id=current_user.id).first()
        if not extra:
            flash(
                "You can't participate to {0} because you didn't add your extra details , please go to <a href='{1}'>profile</a> to add it".format(
                    appt.promo_title, url_for('account.change_extra_details')), 'warning')
            return redirect(url_for('promos.promos_list'))
        submissions = Submission.query.filter(Submission.promo_id == appt.id).all()
        submissions = [appt.user_id for appt in submissions]
        if current_user.id in submissions:
            flash("You have <strong>already participated</strong> for {0}.".format(appt.promo_title), 'warning')
            return redirect(url_for('promos.promos_list'))
        else:
            appts = Submission(promo_id=appt.id, user_id=current_user.id)
            db.session.add(appts)
            db.session.commit()
            flash("You have successfully participated to {0}.".format(appt.promo_title), 'success')
            return redirect(url_for('promos.promos_list'))


@promos.route('/some-endpoint', methods=['POST'])
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
