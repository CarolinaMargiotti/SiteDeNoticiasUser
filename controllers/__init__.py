import os
from flask import Blueprint, current_app, make_response,request

from controllers.news_controller import home as news_home
from controllers.news_controller import newsPost as news_post
from controllers.subjects_controller import subjectsList as subjects_list
from controllers.subjects_controller import newsBySubjects as news_by_subjects
from controllers.subjects_controller import getSubjects

from models.envVariables import serviceUrl,projectUrl


template_dir = os.path.abspath('sitedenoticiasuser/templates/')

news_bp = Blueprint("news",__name__,template_folder=template_dir)
subjects_bp = Blueprint("subjects",__name__,template_folder=template_dir)

def envVariablesDict():
    res = getSubjects(1,3)
    return dict(subjectsListForMenu=res,serviceUrl=serviceUrl,projectUrl=projectUrl)


@news_bp.context_processor
def inject_news_subjects():
    return envVariablesDict()


@subjects_bp.context_processor
def inject_news_subjects():
    return envVariablesDict()



@news_bp.route("/")
def home():
    req = request.args
    pageNumber = req.get("pageNumber",1)
    limit = req.get("limit",4)

    return news_home(limit,pageNumber)

@news_bp.route("/newsPost/<int:postId>")
def newsPost(postId):
    return news_post(postId)


@subjects_bp.route("/homesubject/<string:subject>")
def subjectsList(subject):
    req = request.args
    pageNumber = req.get("pageNumber",1)
    limit = req.get("limit",4)
    return news_by_subjects(pageNumber,limit,subject)

@subjects_bp.route("/homesubject")
def homeSubject():
    req = request.args
    pageNumber = req.get("pageNumber",1)
    limit = req.get("limit",4)
    return subjects_list(pageNumber,limit)
