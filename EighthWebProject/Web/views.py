from django.shortcuts import render

# Create your views here.
def list1(request):
    things = ['Green Rat','Red Bat','Blue Cat','Green Ball','Red Pen','Blue Pencil','Green Chili', 'Red Tomato','Blue Brinjal']
    context= {
        'things': things,
        }
    return render(request, 'list1.html', context)

def list2(request):
    things = ['Green Rat','Red Bat','Blue Cat','Green Ball','Red Pen','Blue Pencil','Green Chili', 'Red Tomato','Blue Brinjal']
    context= {
        'things': things,
        }
    return render(request, 'list2.html', context)

def list3(request):
    things = ['Green Rat','Red Bat','Blue Cat','Green Ball','Red Pen','Blue Pencil','Green Chili', 'Red Tomato','Blue Brinjal']
    """ g = [things[0], things[3], things[6]]
    r = [things[1], things[4], things[7]]
    b = [things[2], things[5], things[8]] """
    
    g = []
    r = []
    b = []

    i = 0
    j = 1
    k = 2
    
    while i < len(things):
        g.append(things[i])
        i = i + 3
    while j < len(things):
        r.append(things[j])
        j = j + 3
    while k < len(things):
        b.append(things[k])
        k = k + 3

    context= {
        'things': things,
        'data': zip(g,r,b),
        }
    return render(request, 'list3.html', context)