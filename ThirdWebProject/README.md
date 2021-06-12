#### 3. ThirdWebProject
##### Title: 3Django_SimpleHTMLPage_CSS_Connectivity
It is about how to add CSS file and how to render it on Webpage.

Prerequisite: Just go through with my previous repository "1Django_SimpleHTMLPage_Connectivity" to understand the connectivity.

2 ways are exists to run CSS scripts on Webpage via Django Platform:
1. given by PATH
2. given by django built in template tags which starts and ends with {}

So, to understand the directory nature
we have templates folder in which index.html exists
we have statics folder in which we have css folder which contains style.css file
Okay.

I have attached both HTML and CSS Files in the repository.

So, in settings.py you have to add these lines:

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'statics')
]

I have attached ""settings.py" in repository to understand where I put these lines.

So,
    
###### Given by Path: 
You can add css script in html file like this:

    <link rel="stylesheet" href="/static/css/style.css">

###### Given by django built in template tags:
In the head tag; add 

{% load static %}
    
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    
   
I have attached these 2 ways in index.html and index1.html(while running the code; make sure you keep only one file and having name "index.html".

ProjectName: ThirdWebProject

ApplicationName: Web 
