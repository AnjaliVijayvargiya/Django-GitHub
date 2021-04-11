from django.shortcuts import render

# Create your views here.
def Addition(request):
    return render(request, 'Addition.html')

def Subtraction(request):
    return render(request, 'Subtraction.html')

def Multipication(request):
    return render(request, 'Multipication.html')

def Dividation(request):
    return render(request, 'Dividation.html')

def output(request):
    if request.method == "POST":
        if(request.POST['actt'] == 'Add'):
            a = int(request.POST['input1'])
            b = int(request.POST['input2'])
            c = a+b
            print(c)
            return render(request,'Addition.html',{'A':a,'B':b,'Result':c})
        elif(request.POST['actt'] == 'Subtract'):
            a = int(request.POST['input1'])
            b = int(request.POST['input2'])
            c = a-b
            print(c)
            return render(request,'Subtraction.html',{'A':a,'B':b,'Result':c})
        elif(request.POST['actt'] == 'Multiply'):
            a = int(request.POST['input1'])
            b = int(request.POST['input2'])
            c = a*b
            print(c)
            return render(request,'Multipication.html',{'A':a,'B':b,'Result':c})
        elif(request.POST['actt'] == 'Divide'):
            a = int(request.POST['input1'])
            b = int(request.POST['input2'])
            c = a/b
            print(c)
            return render(request,'Dividation.html',{'A':a,'B':b,'Result':c})
        else:
           return render(request,'Addition.html') 
    else:
       return render(request,'Subtraction.html')