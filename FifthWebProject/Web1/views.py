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