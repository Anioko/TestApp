from flask import Blueprint, render_template, abort, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_required
from bs4 import BeautifulSoup
import json
import requests
from app.models import *
import app.scrapper as scrapper
from apscheduler.schedulers.background import BackgroundScheduler


crawlers = Blueprint('crawlers', __name__)


@crawlers.route('/crawl/')
def crawl_list():
    # api-endpoint 
    URL = "https://api.jobspikr.com/v2/data"
    # defining a params dict for the parameters to be sent to the API 
    auth=('mediv_jp_46f882f1a7', 'pCU_fcC0xqzymqnAIgA9WIvxtlc7qXb5W1rQ2mT1tCk')
    headers = {"Content-Type": "application/json"}
    ### Use this size to limit the quantity of jobs
    data_body = {"search_query_json": {"bool": {"must": [{"query_string": {"default_field": "job_title","query": "\"registered nurse\" OR \"nurse\" OR \"physician\" OR \"doctor\""}},{"query_string": {"default_field": "job_type","query": "*"}},{"query_string": {"default_field": "company_name","query": "*"}},{"bool": {"should": [{"bool": {"must": [{"query_string": {"fields": ["country","inferred_country"],"query": "\"United States\" OR \"USA\" OR \"United States\" OR \"US\""}}]}},{"bool": {"must": [{"query_string": {"fields": ["country","inferred_country"],"query": "\"United Kingdom\" OR \"England\" OR \"Scotland\" OR \"Northern Ireland\" OR \"Wales\" OR \"UK\" OR \"United Kingdom\""}}]}},{"bool": {"must": [{"query_string": {"fields": ["country","inferred_country"],"query": "\"Canada\""}}]}}]}},{"exists": {"field": "salary_offered"}},{"bool": {"should": [{"exists": {"field": "contact_phone_number"}},{"exists": {"field": "contact_email"}}]}},{"query_string": {"default_field": "has_expired","query": False}},{"range": {"post_date": {"gte": "2020-03-20","lte": "2020-03-27"}}}],"must_not": [{"query_string": {"default_field": "company_name","query": "Unspecified"}}]}}}
    ###data_body = {"size": 1000,"search_query_json": {"bool": {"must": [{"query_string": {"default_field": "job_title","query": "\"nurses\" OR \"nurse practitioner\" OR \"medical practitioner\" OR \"medical\" OR \"nurse\" OR \"healthcare\" OR \"health care\" OR \"care\" OR \"doctor\" OR \"physician\""}},{"query_string": {"default_field": "job_type","query": "*"}},{"query_string": {"default_field": "company_name","query": "*"}},{"bool": {"should": [{"bool": {"must": [{"query_string": {"fields": ["country","inferred_country"],"query": "\"United States\" OR \"USA\" OR \"United States\" OR \"US\""}}]}},{"bool": {"must": [{"query_string": {"fields": ["country","inferred_country"],"query": "\"United Kingdom\" OR \"England\" OR \"Scotland\" OR \"Northern Ireland\" OR \"Wales\" OR \"UK\" OR \"United Kingdom\""}}]}},{"bool": {"must": [{"query_string": {"fields": ["country","inferred_country"],"query": "\"Canada\""}}]}}]}},{"exists": {"field": "salary_offered"}},{"bool": {"should": [{"exists": {"field": "contact_phone_number"}},{"exists": {"field": "contact_email"}}]}},{"query_string": {"default_field": "has_expired","query": False}},{"range": {"post_date": {"gte": "2020-02-02","lte": "2020-02-25"}}}],"must_not": [{"query_string": {"default_field": "company_name","query": "Unspecified"}}]}}}
    print("Post is going to start")
    r = requests.post(url = URL, json = data_body, auth = auth, headers = headers) 
    # extracting data in json format 
    data = r.json()["job_data"]
    print(len(data))
    for i in range(0, len(data)):
        date_time = data[i]["post_date"].split("-")
        now = datetime(int(date_time[0]), int(date_time[1]), int(date_time[2]))
        print(now)
        jobpikr=JobPikr(
        job_type = data[i]["job_type"],
        has_expired = data[i]["has_expired"],
        inferred_country = data[i]["inferred_country"],
        country = data[i]["country"],
        crawl_timestamp = data[i]["crawl_timestamp"],
        city = data[i]["city"],
        inferred_city = data[i]["inferred_city"],
        salary_offered = data[i]["salary_offered"],
        url = data[i]["url"],
        contact_email = data[i]["contact_email"],
        uniq_id = data[i]["uniq_id"],
        job_description = data[i]["job_description"],
        inferred_state = data[i]["inferred_state"],
        post_date = str(now),
        company_name = data[i]["company_name"],
        category = data[i]["category"],
        job_title = data[i]["job_title"],
        cursor = data[i]["cursor"]
        )
        db.session.add(jobpikr)
        db.session.commit()
    #Scrapper related
    #sched = BackgroundScheduler(daemon=True)
    #sched.add_job(job_crawlers,'interval',minutes=5)
    #sched.start()
    return render_template('errors/500.html')


#### commented out because it was killing workers and has datetime issues###
##@crawlers.route('/crawl/')
##def crawl_list():
##    #Scrapper related
##    print("Print crawlers started")
##    try:
##        job_crawlers()
##    except Exception as e:
##        print("Not started")
##    print("Print crawlers done")
##    #sched = BackgroundScheduler(daemon=True)
##    try:
##        sched.remove_job(job_crawlers)
##    except:
##        pass
##    #sched.add_job(job_crawlers,'interval',minutes=10)
##    #sched.start()
##    return render_template('errors/500.html')

##
###Scrapper related
##def job_crawlers():
##    #""" Function for test purposes. """
##    try:
##        result_scrapper = scrapper.getJobxoomJobs()
##        for i in range(0, len(result_scrapper)):
##            p,q=getDateTime(result_scrapper[i]["start"],result_scrapper[i]["end"])
##            cr_job = Crawledjob(
##            image_filename = result_scrapper[i]["logo"],
##            pub_date = p,
##            end_date = q,
##            job_title = result_scrapper[i]["name"],
##            job_city = result_scrapper[i]["city"],
##            job_state = result_scrapper[i]["state"],
##            job_country = result_scrapper[i]["country"],
##            description = result_scrapper[i]["desc"],
##            company_name = result_scrapper[i]["organization"],
##            job_url = result_scrapper[i]["link"]
##            )
##            db.session.add(cr_job)
##        db.session.commit()
##        print("Jobxoom done")
##        flash('Data added!', 'success')
##        result_scrapper = scrapper.getJobvertiseJobs()
##        for i in range(0, len(result_scrapper)):
##            p,q=getDateTime(result_scrapper[i]["start"],result_scrapper[i]["end"])
##            cr_job = Crawledjob(
##            image_filename = result_scrapper[i]["logo"],
##            pub_date = p,
##            end_date = q,
##            job_title = result_scrapper[i]["name"],
##            job_city = result_scrapper[i]["city"],
##            job_state = result_scrapper[i]["state"],
##            job_country = result_scrapper[i]["country"],
##            description = result_scrapper[i]["desc"],
##            company_name = result_scrapper[i]["organization"],
##            job_url = result_scrapper[i]["link"]
##            )
##            db.session.add(cr_job)
##        db.session.commit()
##        flash('Data added!', 'success')
##        print("Jobvertise done")
##    except Exception as e:
##        print(e)
##
##def getDateTime(start, end):
##    st_date, end_date = "", ""
##    if start:
##        st = start.split(" ")
##        for s in range(0, len(st)):
##            try:
##                x1 = datetime.datetime.now()
##                y = int(s)
##                if "year" in start:
##                    x = datetime.datetime((x1.year-y), x1.month, x1.day)
##                    st_date = str(x)
##                elif "month" in start:
##                    x = datetime.datetime(x1.year, (x1.month-y), x1.day)
##                    st_date = str(x)
##                elif "day" in start:
##                    x = datetime.datetime(x1.year, x1.month, (x1.day-y))
##                    st_date = str(x)
##                if not end:
##                    end_date = st_date + datetime.timedelta(days=30)
##            except:
##                pass
##    if end:
##        st = start.split(" ")
##        for s in range(0, len(st)):
##            try:
##                x1 = datetime.datetime.now()
##                y = int(s)
##                if "year" in end:
##                    x = datetime.datetime((x1.year-y), x1.month, x1.day)
##                    end_date = str(x)
##                elif "month" in end:
##                    x = datetime.datetime(x1.year, (x1.month-y), x1.day)
##                    end_date = str(x)
##                elif "day" in end:
##                    x = datetime.datetime(x1.year, x1.month, (x1.day-y))
##                    end_date = str(x)
##                if not start:
##                    st_date = end_date + datetime.timedelta(days=30)
##            except:
##                pass
##    return st_date,end_date

