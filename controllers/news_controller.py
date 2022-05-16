from flask import jsonify, render_template
import requests
from controllers.subjects_controller import getAllSubjects

#import dos models
from models.news import news as noticias

baseUrl="http://127.0.0.1:8080"

def getNews(startNumber,limit):
    try:
        response = requests.get(f'{baseUrl}/getallnews?startNumber={startNumber}&quantity={limit}')
        return response.json()
    except:
        return {}

def getNewsPost(id):
    try:
        response = requests.get(f'{baseUrl}/getnews?id={id}')
        return response.json()
    except:
        return {}

#retorno dos templates

def home(limit,pageNumber):
    startNumber = (int(limit)*int(pageNumber))-(int(limit)-1)
    noticias=getNews(startNumber,limit)
    assuntos = getAllSubjects()
    return render_template("home.html",newsList=noticias,subjects=assuntos,pageNumber=pageNumber,quantity=limit)


def newsPost(id):
    noticia = getNewsPost(id)
    assuntos = getAllSubjects()
    return render_template("newsPost.html",newsDetails=noticia,subjects=assuntos)