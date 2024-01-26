from django.shortcuts import render , HttpResponse
from datetime import datetime
# Create your views here.

def homepage(request):
    return render(request, "base.html")

def display_date(request):
    day = datetime.today().day
    month = datetime.today().month
    year = datetime.today().year
    date = f"Date: {day}, {month}, {year}"
    return HttpResponse(date)


def info(request): 
    # request info and attriutes 

    path = request.path 
    method = request.method 
    address = request.META['REMOTE_ADDR']
    scheme = request.scheme
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    content=f''' 
        <center>
        <h2>Testing Django Request Response Objects</h2> 
        <p>Request path : " {path}</p> 
        <p>Request Method :{method}</p>
        <p>Request Address : {address}</p>
        <p>Request scheme : {scheme}</p>
        <p>Request user_agent : {user_agent}</p>
        <p>Request Path-info : {path_info}</p>
        </center> 
    '''
    return HttpResponse(content) 

def getname(request, name, id):
    name_n_details= {
        "uzair":"Hello my name is uzair, i am pursuing computer engineering",
        "shamir":"hello my name is shamir i am pursuing industrial engineering",
        "rimsha":"hello my name is Rimsha i am pursuing MBBS",
        "zain":"hello my name is zain i am pursuing CA",
        "Anas":"hello my name is Anas",
    }

    details = name_n_details[name]

    content = f'''<center>
                <h1>{name}</h1>
                <p> {details}</p></center>'''

    return HttpResponse(content)

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        content = f"Name: {name}, ID: {id}"
        return HttpResponse(content)

#calling the modelform
from myapp.forms import logForm

def index(request): 
    form = logForm()
    if request.method == "POST":
        form = logForm(request.POST) # update the form objects with the contents of post inside the request object  
        if form.is_valid():
            form.save()
    context = {'form': form}

    return render(request, 'form.html', context)    


from myapp.models import Person

def details_of_user(requests):
    '''display the name in details.html'''
    names = Person.objects.all()
    content = {'details': names}

    return render(requests, 'details.html', content)

def home(requests):
    return render(requests, 'home.html', {})