from flask import Blueprint, render_template, abort, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_required

from app.models import *
from datetime import datetime, timedelta, date


jobs = Blueprint('jobs', __name__)


@jobs.route('/list/')
def jobs_list():
    appts = Job.query.filter(Job.organisation != None).filter(Job.end_date >= datetime.now()).order_by(Job.pub_date.asc()).all()
    #jobs = JobPikr.query.filter(JobPikr.has_expired == "false").all()
    jobs = JobPikr.query.filter(JobPikr.company_name != None).filter(JobPikr.crawl_timestamp >= (date.today()-timedelta(days=40)).isoformat()).order_by(JobPikr.job_title.asc()).all()
    #crawlers = Crawledjob.query.filter(Crawledjob.company_name != None).filter(Crawledjob.created_at >= duration).order_by(Crawledjob.job_title.asc()).all()
    return render_template('jobs/alljobs.html', appts=appts, jobs=jobs)#crawlers=crawlers, jobs=jobs)


@jobs.route('/c/<int:job_id>/<job_title>/<job_city>/<job_state>/<job_country>')
def crawled_job_details(job_id, job_title, job_city, job_state, job_country):
    appts = Crawledjob.query.filter(Crawledjob.id == job_id).first_or_404()
    return render_template('jobs/crawled_job_details.html', appt=appts)


@jobs.route('/<int:job_id>/<job_title>/<city>/')
def jobpikr_details(job_id, job_title, city):
    appts = JobPikr.query.filter(JobPikr.job_title == job_title).first_or_404()
    return render_template('jobs/jobspikr_details.html', appt=appts)


@jobs.route('/<int:position_id>/<position_title>/<position_city>/<position_state>/<position_country>')
def job_details(position_id, position_title, position_city, position_state, position_country):
    appts = Job.query.filter(Job.id == position_id).first_or_404()
    org_users = User.query.all()
    orgs = Organisation.query.filter(Organisation.user_id == User.id).all()
    return render_template('jobs/job_details.html', appt=appts, orgs=orgs, org_users=org_users)


@jobs.route('/<int:position_id>/<position_title>/apply')
@login_required
def job_apply(position_id, position_title):
    appt = db.session.query(Job).get(position_id)
    if appt is None:
        abort(404)
    elif current_user.id is None:
        abort(403)
    else:
        if appt.creator == current_user:
            flash("You Can't Apply to {0} because you created it".format(appt.position_title), 'warning')
            return redirect(url_for('jobs.jobs_list'))
        extra = Extra.query.filter_by(user_id=current_user.id).first()
        if not extra:
            flash(
                "You can't apply to {0} because you didn't add your extra details , please go to <a href='{1}'>Profile</a> to add it".format(
                    appt.position_title, url_for('account.change_extra_details')), 'warning')
            return redirect(url_for('jobs.jobs_list'))
        applications = Application.query.filter(Application.position_id == appt.id).all()
        applicants = [appt.user_id for appt in applications]
        if current_user.id in applicants:
            flash("You have <strong>already applied</strong> for {0}.".format(appt.position_title), 'warning')
            return redirect(url_for('jobs.jobs_list'))
        else:
            appts = Application(position_id=appt.id, user_id=current_user.id)
            db.session.add(appts)
            db.session.commit()
            flash("You have successfully applied to {0}.".format(appt.position_title), 'success')
            return redirect(url_for('jobs.jobs_list'))


@jobs.route('/some-endpoint', methods=['POST'])
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
