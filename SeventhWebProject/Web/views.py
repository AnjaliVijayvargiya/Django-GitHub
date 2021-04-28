from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    person= {'firstname': 'Amrinder', 'lastname': 'Kaur'}
    age = 27
    hobbies = ['Dancing', 'Singing', 'Playing Sports']
    context= {
        'person': person,
        'age': age,
        'hobbies': hobbies,
        }
    return render(request, 'index.html', context)

def about(request):
    person= {'firstname': 'Sukhvinder', 'lastname': 'Kaur'}
    age = 32
    hobbies = ['Coding', 'Programming', 'Editing']
    context= {
        'person': person,
        'age': age,
        'hobbies': hobbies,
        }
    return render(request, 'about.html', context)

def contact(request):
    person= {'firstname': 'Parminder', 'lastname': 'Kaur'}
    age = 19
    hobbies = ['Watching Movies', 'Listening Songs', 'Playing Guitar']
    context= {
        'person': person,
        'age': age,
        'hobbies': hobbies,
        }
    return render(request, 'contact.html', context)