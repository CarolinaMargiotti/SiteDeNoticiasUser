from flask import  jsonify, render_template
import requests
from models.envVariables import serviceUrl

def getSubjects(startNumber,limit):
    try:
        response = requests.get(f"{serviceUrl}/getsubjects?startNumber={startNumber}&quantity={limit}")
        return response.json()
    except:
        return []

def getAllSubjects():
    try:
        response = requests.get(f"{serviceUrl}/getallsubjects")
        return response.json()
    except:
        return []

def getSubjects(startNumber,limit):
    try:
        response = requests.get(f"{serviceUrl}/getsubjects?startNumber={startNumber}&quantity={limit}")
        return response.json()
    except:
        return []

def getSubjectById(id):
    try:
        response = requests.get(f"{serviceUrl}/getnewsbyid?id={id}")
        return response.json()
    except:
        return {}

def getNewsSubjects(startNumber,limit,subject):
    try:
        response = requests.get(f'{serviceUrl}/getallnewsbysubject?startNumber={startNumber}&quantity={limit}&assunto={subject}')
        return response.json()
    except:
        return []

def subjectsList(pageNumber,limit):
    startNumber = (int(limit)*int(pageNumber))-(int(limit)-1)
    assuntos = getSubjects(startNumber,limit)
    return render_template("homeSubjects.html",subjects=assuntos,pageNumber=pageNumber,quantity=limit)

def newsBySubjects(startNumber,limit,subject):
    assunto = getSubjectById(subject)
    noticias = getNewsSubjects(startNumber,limit,subject)
    return render_template("newsBySubjects.html",newsList=noticias,subject=assunto)