#### 1. FirstWebProject
##### Title: 1Django_SimpleHTMLPage_Connectivity
It is about how to connect a simple HTML Webpage with Django Framework. It is an step by step approach.

First of all; 
###### Prerequisite:
Make sure you have all this libararies installed on your system
1. Python 3.7 (django library easily installed when you have this version)
set Environmental variables for python
2. Numpy (for future references)
3. Pandas (for future references)
4. Django
python -m pip install django

When django is successfully installed

###### Steps:
1. open CMD Prompt
2. Create your main directory (I created on my Desktop location)
3. follow These Steps
C:\Users\Anjali>cd Desktop

C:\Users\Anjali\Desktop>mkdir Django_Web_Project

C:\Users\Anjali\Desktop>cd Django_Web_Project

C:\Users\Anjali\Desktop\Django_Web_Project>django-admin startproject FirstWebProject

C:\Users\Anjali\Desktop\Django_Web_Project>cd FirstWebProject

C:\Users\Anjali\Desktop\Django_Web_Project\FirstWebProject>python manage.py startapp Web1

C:\Users\Anjali\Desktop\Django_Web_Project\FirstWebProject>

Here; ProjectName: FirstWebProject
ApplicationName: Web1

4. Open the project folder in VS code

For proceed further; 2 terms you need to know when creating a web project. Website containes HTML, CSS, JS files mainly. We add HTML files in templates folder and add this path in settings.py. and we add CSS and JS file in statics folder and add this link also in settings.py. How?? we will see soon.

Now, create 2 folder "templates" and "statics" in project folder or where manage.py exists.

create index.html file in "templates" folder. this is the file for your website. (homepage)

I have attached index.html file for your reference. we will work on static folder in future.

Now, in settings.py, add 'templates'(same name as of your folder) in TEMPLATES like this

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

Save files.
In Views.py; which exists on Application Folder "Web1"
Edit like this

from django.shortcuts import render

def home(request):

    return render(request, 'index.html')
    
Save this file.

Now, in urls.py; which exists on Project Folder "FirstWebProject"
Edit like this

from django.contrib import admin

from django.urls import path

from Web1 import views 
 
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home)
]

Save this file too.

And in the last, run the following command in VS Terminal
python manage.py runserver
and Click on the IP Address Link; You will get the HTML Page which is rendering on the webBrowser.

ProjectName: FirstWebProject

ApplicationName: Web1
