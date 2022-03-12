from flask import request, jsonify, render_template

#import dos models

noticias = [{'titulo':"porquinhos da india",'assunto':"pets",'conteudo':"cuicuicuicuicui"}]

def getNews():
    return noticias

def getNewsPost(id):
    return noticias[id]

#retorno dos templates
def home():
    noticias=getNews()
    return render_template("home.html",newsList=noticias)

def newsPost(id):
    noticia = getNewsPost(id)
    return render_template("newsPost.html",newsDetails=noticia)