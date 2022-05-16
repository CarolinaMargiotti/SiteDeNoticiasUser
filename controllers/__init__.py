import os
from flask import Blueprint, current_app,request

from controllers.news_controller import home as news_home
from controllers.news_controller import newsPost as news_post
from controllers.news_controller import homeSubject as news_home_subject

template_dir = os.path.abspath('sitedenoticiasuser/templates/')

news_bp = Blueprint("news",__name__,template_folder=template_dir)

@news_bp.route("/")
def home():
    req = request.args
    pageNumber = req.get("pageNumber",1)
    limit = req.get("limit",4)

    return news_home(limit,pageNumber)

@news_bp.route("/<string:subject>")
def homeSubject(subject):
    return news_home_subject(subject)

@news_bp.route("/newsPost/<int:postId>")
def newsPost(postId):
    return news_post(postId)

