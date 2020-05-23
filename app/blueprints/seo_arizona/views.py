from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user

seo_arizona = Blueprint('seo_arizona', __name__)

@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Phoenix')
def landing_usa_arizona_0():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Phoenix")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Tucson')
def landing_usa_arizona_1():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Tucson")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Mesa')
def landing_usa_arizona_2():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Mesa")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Chandler')
def landing_usa_arizona_3():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Chandler")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Glendale')
def landing_usa_arizona_4():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Glendale")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Scottsdale')
def landing_usa_arizona_5():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Scottsdale")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Gilbert')
def landing_usa_arizona_6():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Gilbert")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Tempe')
def landing_usa_arizona_7():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Tempe")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Peoria')
def landing_usa_arizona_8():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Peoria")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Surprise')
def landing_usa_arizona_9():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Surprise")

@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Yuma')
def landing_usa_arizona_10():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Yuma")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Avondale')
def landing_usa_arizona_12():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Avondale")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Flagstaff')
def landing_usa_arizona_13():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Flagstaff")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Goodyear')
def landing_usa_arizona_14():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Goodyear")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Lake Havasu City')
def landing_usa_arizona_15():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Lake Havasu City")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Buckeye')
def landing_usa_arizona_16():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Buckeye")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Casa Grande')
def landing_usa_arizona_17():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Casa Grande")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Sierra Vista')
def landing_usa_arizona_18():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Sierra Vista")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Maricopa')
def landing_usa_arizona_19():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Maricopa")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Oro Valley')
def landing_usa_arizona_20():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Oro Valley")

@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Prescott')
def landing_usa_arizona_21():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Prescott")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Bullhead City')
def landing_usa_arizona_23():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Bullhead City")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Prescott Valley')
def landing_usa_arizona_24():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Prescott Valley")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Apache Junction')
def landing_usa_arizona_25():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website", location="Apache Junction")
@seo_arizona.route('/healthcare-professional-community-and-social-networking-website/Marana')
def landing_usa_arizona_27():
    return render_template('public/seo_arizona.html', keyword="healthcare professional community and social networking website ", location="Marana")

#######Recruiters in Arizona #####

@seo_arizona.route('/find-healthcare-professionals-get-cv/Phoenix')
def recruiters_usa_arizona_0():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Phoenix")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Tucson')
def recruiters_usa_arizona_1():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Tucson")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Mesa')
def recruiters_usa_arizona_2():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Mesa")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Chandler')
def recruiters_usa_arizona_3():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Chandler")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Glendale')
def recruiters_usa_arizona_4():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Glendale")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Scottsdale')
def recruiters_usa_arizona_5():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Scottsdale")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Gilbert')
def recruiters_usa_arizona_6():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Gilbert")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Tempe')
def recruiters_usa_arizona_7():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Tempe")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Peoria')
def recruiters_usa_arizona_8():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Peoria")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Surprise')
def recruiters_usa_arizona_9():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Surprise")

@seo_arizona.route('/find-healthcare-professionals-get-cv/Yuma')
def recruiters_usa_arizona_10():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Yuma")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Avondale')
def recruiters_usa_arizona_12():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Avondale")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Flagstaff')
def recruiters_usa_arizona_13():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Flagstaff")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Goodyear')
def recruiters_usa_arizona_14():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Goodyear")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Lake Havasu City')
def recruiters_usa_arizona_15():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Lake Havasu City")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Buckeye')
def recruiters_usa_arizona_16():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Buckeye")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Casa Grande')
def recruiters_usa_arizona_17():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Casa Grande")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Sierra Vista')
def recruiters_usa_arizona_18():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Sierra Vista")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Maricopa')
def recruiters_usa_arizona_19():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Maricopa")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Oro Valley')
def recruiters_usa_arizona_20():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Oro Valley")

@seo_arizona.route('/find-healthcare-professionals-get-cv/Prescott')
def recruiters_usa_arizona_21():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Prescott")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Bullhead City')
def recruiters_usa_arizona_23():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Bullhead City")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Prescott Valley')
def recruiters_usa_arizona_24():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Prescott Valley")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Apache Junction')
def recruiters_usa_arizona_25():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals", location="Apache Junction")
@seo_arizona.route('/find-healthcare-professionals-get-cv/Marana')
def recruiters_usa_arizona_27():
    return render_template('public/recruiters_arizona.html', keyword="healthcare professionals ", location="Marana")


#######Registered Nurse Social Network #####

@seo_arizona.route('/registered-nurse-RN-professional-social-network/Phoenix')
def landing_usa_arizona_registered_nurse_0():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Phoenix")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Tucson')
def landing_usa_arizona_registered_nurse_1():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Tucson")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Mesa')
def landing_usa_arizona_registered_nurse_2():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Mesa")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Chandler')
def landing_usa_arizona_registered_nurse_3():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Chandler")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Glendale')
def landing_usa_arizona_registered_nurse_4():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Glendale")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Scottsdale')
def landing_usa_arizona_registered_nurse_5():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Scottsdale")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Gilbert')
def landing_usa_arizona_registered_nurse_6():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Gilbert")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Tempe')
def landing_usa_arizona_registered_nurse_7():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Tempe")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Peoria')
def landing_usa_arizona_registered_nurse_8():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Peoria")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Surprise')
def landing_usa_arizona_registered_nurse_9():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Surprise")

@seo_arizona.route('/registered-nurse-RN-professional-social-network/Yuma')
def landing_usa_arizona_registered_nurse_10():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Yuma")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Avondale')
def landing_usa_arizona_registered_nurse_12():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Avondale")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Flagstaff')
def landing_usa_arizona_registered_nurse_13():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Flagstaff")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Goodyear')
def landing_usa_arizona_registered_nurse_14():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Goodyear")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Lake Havasu City')
def landing_usa_arizona_registered_nurse_15():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Lake Havasu City")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Buckeye')
def landing_usa_arizona_registered_nurse_16():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Buckeye")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Casa Grande')
def landing_usa_arizona_registered_nurse_17():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Casa Grande")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Sierra Vista')
def landing_usa_arizona_registered_nurse_18():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Sierra Vista")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Maricopa')
def landing_usa_arizona_registered_nurse_19():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Maricopa")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Oro Valley')
def landing_usa_arizona_registered_nurse_20():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Oro Valley")

@seo_arizona.route('/registered-nurse-RN-professional-social-network/Prescott')
def landing_usa_arizona_registered_nurse_21():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Prescott")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Bullhead City')
def landing_usa_arizona_registered_nurse_23():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Bullhead City")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Prescott Valley')
def landing_usa_arizona_registered_nurse_24():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Prescott Valley")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Apache Junction')
def landing_usa_arizona_registered_nurse_25():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network", location="Apache Junction")
@seo_arizona.route('/registered-nurse-RN-professional-social-network/Marana')
def landing_usa_arizona_registered_nurse_27():
    return render_template('public/seo_arizona.html', keyword="registered nurse (RN) professional social network ", location="Marana")


