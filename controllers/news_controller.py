from flask import jsonify, render_template
import requests
from controllers.subjects_controller import getAllSubjects


#import dos models
from models.news import news as noticias

baseUrl="http://127.0.0.1:8080"

assuntos = ['pets','arte','geek']

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

def getSubjects():
    return assuntos

def getSubjectFromId(id):
    return assuntos[id]

def getNewsSubjects(subject):
    noticias=[]
    # for news in getNews():
    #     if news['assunto'] == subject:
    #         noticias.append(news)
    return noticias

#retorno dos templates

def home(limit,pageNumber):
    noticias=getNews(pageNumber,limit)
    assuntos = getAllSubjects()
    return render_template("home.html",newsList=noticias,subjects=assuntos)

def homeSubject(subject):
    noticias = getNewsSubjects(subject)
    return render_template("homeSubject.html",newsList=noticias,subject=subject)

def newsPost(id):
    noticia = getNewsPost(id)
    assuntos = getAllSubjects()
    return render_template("newsPost.html",newsDetails=noticia,subjects=assuntos)