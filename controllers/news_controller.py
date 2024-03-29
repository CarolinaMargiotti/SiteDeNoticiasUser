from flask import jsonify, render_template
import requests
from controllers.subjects_controller import getAllSubjects
from models.envVariables import serviceUrl

def getNews(startNumber,limit):
    try:
        response = requests.get(f'{serviceUrl}/getallnews?startNumber={startNumber}&quantity={limit}')
        return response.json()
    except:
        return {}

def getNewsPost(id):
    try:
        response = requests.get(f'{serviceUrl}/getnews?id={id}')
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