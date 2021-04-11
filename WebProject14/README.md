#### 14. WebProject14
###### Title: 14Django_Rendering_Forms_InVariousWays
A Mini Project on how to render forms in Django. In this, a simple form is made for collecting entries and displaying them after submitting these entries. There are 4 ways exists to render the Django forms. I have implemented all these in this project.
1. Render Django Forms as unordered list
2. Render Django Forms as paragraph
3. Render Django Forms as table
4. Render Django Form Fields Manually

I have commented in the above 3 ways for checking the working of the last way(Manually). If you want to check another specific way, just uncomment that way and comment the remainings ways.(You can have this idea by the code itself)


While implementating this project, I have learnt some things:
1. How to render forms using models.py and forms.py.
2. How to call them in views.py
3. Connect the views in urls.py
4. How to createsuperuser to see the admin page for watching the records in the database as well.
7. You can see admin page by the runserver-url/admin.
8. Understand the concept of form.as_p; form.as_table; form.as_ul.
9. Use of *args and ** kwargs in Python
10. Do not forget to call two commands after creation of model:
    1. python manage.py makemigrations
    2. python manage.py migrate
    3. then call; python manage.py runserver

ProjectName: WebProject14

ApplicationName: Web

###### Links:
1. https://www.geeksforgeeks.org/django-forms/
2. https://www.geeksforgeeks.org/django-forms/#form-fields
3. https://www.geeksforgeeks.org/form-as_ul-render-django-forms-as-list/
4. https://www.geeksforgeeks.org/form-as_p-render-django-forms-as-paragraph/
5. https://www.geeksforgeeks.org/form-as_table-render-django-forms-as-table/
6. https://www.geeksforgeeks.org/render-django-form-fields-manually/
7. https://www.geeksforgeeks.org/args-kwargs-python/


###### Result:
![](Results/WebProject14.png)

