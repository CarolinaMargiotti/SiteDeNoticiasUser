from flask import request, jsonify, render_template

#import dos models

noticias = [
{'id':0,'titulo':"porquinhos da india",'assunto':"pets",'conteudo':"cuicuicuicuicui"},
{'id':1,'titulo':"cobrinha",'assunto':"pets",'conteudo':"ssssssssssssss"},
{'id':2,'titulo':"macaco",'assunto':"pets",'conteudo':"uh uh uh uh"},
{'id':3,'titulo':'art nouvelle','assunto':'arte','conteudo':'arte dos elfos'},
{'id':4,'titulo':'arte barroca','assunto':'arte','conteudo':'materia da escola'},
{'id':5,'titulo':'lançamento elden ring','assunto':'geek','conteudo':'é um jogo que lançou'},
{'id':6,'titulo':'sonic é bom','assunto':'geek','conteudo':'gotta go fast'},
]
assuntos = ['pets','arte']

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