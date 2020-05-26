from flask import Blueprint, render_template, abort, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_required

from app.models import *

professionals = Blueprint('professionals', __name__)


@professionals.route('/<opportunity_id>/add/', methods=['Get', 'POST'])
@login_required
def create_opportunity(opportunity_id):
    opp = Opportunity.query.filter_by(user_id=current_user.id).filter_by(id=opp_id).first_or_404()
    form = OpportunityForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            appt = Opportunity(title=form.title.data,
                       user_id=current_user.id,
                       city=form.city.data,
                       state=form._state.data,
                       country=form.country.data,
                       description=form.description.data,
                       start_date=form.start_date.data.strftime('%d %B, %Y'),  # ''' ##('%Y-%m-%d') Alternative '''
                       end_date=form.end_date.data.strftime('%d %B, %Y'),  # ''' ##('%Y-%m-%d') Alternative '''
                       title=form.title.data,
                       summary=form.summary.data,
                       opportunity_type=form.opportunity_type.data,
                       available_now=form.available_now.data,
                       location_type=form.location_type.data, 
                       )
            db.session.add(appt)
            db.session.commit()
            flash('Opportunity added!', 'success')
            return redirect(url_for('professionals.opportunity_details', opportunity_id=appt.id, title=appt.title,
                                    city=appt.city, state=appt.state,
                                    country=appt.country))
        else:

            flash('ERROR! Opportunity was not added.', 'error')
    return render_template('professionals/create_opportunity.html', form=form, opp=opp)

@professionals.route('/list/')
def opportunity_list():
    #appts = Professionals.query.filter(Professionals.organisation != None).filter(Professionals.end_date >= datetime.now()).order_by(Professionals.pub_date.asc()).all()
    #return render_template('professionals/allprofessionals.html', appts=appts)
    #def professionals_list():
    appts = Opportunity.query.filter(Opportunity.end_date >= datetime.now()).order_by(Opportunity.pub_date.asc()).all()
    return render_template('professionals/allopportunities.html', appts=appts)




@professionals.route('/<int:opportunity_id>/<title>/<city>/<state>/<country>')
def opportunity_details(opportunity_id, title, city, state, country):
    appts = Opportunity.query.filter(Opportunity.id == opportunity_id).first_or_404()
    org_users = User.query.all()
    orgs = Opportunity.query.filter(Opportunity.user_id == User.id).all()
    return render_template('professionals/opportunities_details.html', appt=appts, orgs=orgs, org_users=org_users)




##@professionals.route('/<int:professionals_id>/<professionals_title>/apply')
##@login_required
##def professionals_apply(professionals_id, professionals_title):
##    appt = db.session.query(Professionals).get(professionals_id)
##    if appt is None:
##        abort(404)
##    elif current_user.id is None:
##        abort(403)
##    
##    else:
##        
##        if appt.creator == current_user:
##            flash("You can't apply to {0} because you created it".format(appt.professionals_title), 'warning')
##            return redirect(url_for('professionals.professionals_list'))
##        extra = Extra.query.filter_by(user_id=current_user.id).first()
##        if not extra:
##            flash(
##                "You can't participate to {0} because you didn't add your extra details , please go to <a href='{1}'>profile</a> to add it".format(
##                    appt.professionals_title, url_for('account.change_extra_details')), 'warning')
##            return redirect(url_for('professionals.professionals_list'))
##        submissions = Submission.query.filter(Submission.professionals_id == appt.id).all()
##        submissions = [appt.user_id for appt in submissions]
##        if current_user.id in submissions:
##            flash("You have <strong>already participated</strong> for {0}.".format(appt.professionals_title), 'warning')
##            return redirect(url_for('professionals.professionals_list'))
##        else:
##            appts = Submission(professionals_id=appt.id, user_id=current_user.id)
##            db.session.add(appts)
##            db.session.commit()
##            flash("You have successfully participated to {0}.".format(appt.professionals_title), 'success')
##            return redirect(url_for('professionals.professionals_list'))



