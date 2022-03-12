import os
from flask import Blueprint, current_app

from controllers.news_controller import home as news_home
from controllers.news_controller import newsPost as news_post

template_dir = os.path.abspath('sitedenoticiasuser/templates/')

news_bp = Blueprint("news",__name__,template_folder=template_dir)

@news_bp.route("/")
def home():
    return news_home()

@news_bp.route("/newsPost/<int:postId>")
def newsPost(postId):
    return news_post(postId)

