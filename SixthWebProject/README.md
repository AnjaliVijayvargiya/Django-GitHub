
#### 6. SixthWebProject
##### Title: 6Django_SimpleWebsite_LinkMultiplePages_NavbarLinks_Using_base.html_TemplateInheritance
This is implemented by using base.html file; which contains common properties of all the files including header, footer and navbar.
All the remaining files use this base.html by using this line:

    {% extends 'base.html' %}
    
and we create block snippets for the distinguish part like this in base.html which are called with the values in that other html script in which you want to add data.

    <title> {% block title %}{% endblock title %} | My Website</title>
    
In the other html file, you can call block snippets like this:

    {% extends 'base.html' %}

    {% block title %}Home{% endblock title %}

You can see the code for more understanding.

ProjectName: SixthWebProject

ApplicationName: Web

###### Result:
![](../Results/WebProject5&6.png)
