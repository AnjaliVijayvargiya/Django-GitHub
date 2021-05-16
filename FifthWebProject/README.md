#### 5. FifthWebProject
##### Title: 5Django_SimpleWebsite_LinkMultiplePages_NavbarLinks
In this, I have linked Navbar items and learned how to render various html pages on clicking navbar items.

###### Contents on index.html:

    NavBar with Renamed Items
    Cards in Grid Format
    Link: https://getbootstrap.com/docs/5.0/components/card/
    
###### Ways: 
1. by HttpResponse Method
2. by Render Method

###### Steps:
1. As in the previous repositories, change setting.py and create templates folder
2. In templates folder, create all HTML pages according to your need.
3. Set Urls.py like this

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', views.home, name='home'),
            path('about/', views.about, name='about'),
            path('contact/', views.contact, name='contact'),
        ]
4. Set views.py like this

        from django.shortcuts import render, HttpResponse
        # Create your views here.
        def home(request):
            return render(request,'index.html')

        def about(request):
            #return HttpResponse("This is About Page")
            return render(request,'about.html')

        def contact(request):
            #return HttpResponse("This is Contact Page")
            return render(request,'contact.html')

ProjectName: FifthWebProject

ApplicationName: Web1

###### Result:
![](Results/WebProject5&6.png)
