from flask import request, jsonify, render_template

#import dos models
from models.news import news as noticias

assuntos = ['pets','arte','geek']

def getNews():
    return noticias

def getNewsPost(id):
    return noticias[id]

def getSubjects():
    return assuntos

def getSubjectFromId(id):
    return assuntos[id]

def getNewsSubjects(subject):
    noticias=[]
    for news in getNews():
        if news['assunto'] == subject:
            noticias.append(news)
    return noticias

#retorno dos templates
def home():
    noticias=getNews()
    return render_template("home.html",newsList=noticias)

def homeSubject(subject):
    noticias = getNewsSubjects(subject)
    return render_template("homeSubject.html",newsList=noticias,subject=subject)

def newsPost(id):
    noticia = getNewsPost(id)
    return render_template("newsPost.html",newsDetails=noticia)