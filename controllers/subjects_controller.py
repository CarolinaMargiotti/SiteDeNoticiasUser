from flask import  jsonify, render_template
import requests

baseUrl="http://127.0.0.1:8080"

def getSubjects(startNumber,limit):
    try:
        response = requests.get(f"{baseUrl}/getsubjects?startNumber={startNumber}&quantity={limit}")
        return response.json()
    except:
        return []

def getAllSubjects():
    try:
        response = requests.get(f"{baseUrl}/getallsubjects")
        return response.json()
    except:
        return []

def getSubjectById(id):
    try:
        response = requests.get(f"{baseUrl}/getnewsbyid?id={id}")
        return response.json()
    except:
        return {}