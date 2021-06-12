#### 4. FourthWebProject
##### Title: 4Django_SimpleHTMLPage_CSS_JS_Bootstrap_Connectivity
It is about how to connect JS script in whole package and how to implement in Django Framework.

Prerequisite: Just go through with my previous repositories in sequential manner to understand the connectivity.

2 ways are exists to run JS scripts on Webpage via Django Platform; which is similar as pervious.
1. given by PATH
2. given by django built in template tags which starts and ends with {}

So, to understand the directory nature we have templates folder in which index.html exists we have statics folder in which we have js folder which contains script.js file Okay.

I have attached HTML, CSS and JS Files in the repository for your reference.

So,
    
###### Given by Path: 
You can add js script in html file like this:

    <script src="/static/js/script.js" type="text/javascript"/>

###### Given by django built in template tags:
In the head tag; add 

{% load static %}
    
    <script src="{% static 'js/script.js' %}" type="text/javascript" />

ProjectName: FourthWebProject

ApplicationName: Web 
