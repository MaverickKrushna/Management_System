from django.shortcuts import render , HttpResponse
from datetime import  datetime
from myapp.models import Contact, FaceBook
from django.contrib import messages

# Create your views here.
def index(request):

    context = {
        "variable": "This is the variable krushna  here "
    }

    return render(request , 'index.html', context)

def facebook(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        face_book = FaceBook(user=user , password=password)
        face_book.save()
        messages.success(request , 'activation successfully ')

    return render(request , 'Facebook.html')
    # return HttpResponse("This is the about page ")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        contact = Contact(name=name , email=email , phone=phone ,password=password , date=datetime.today())
        contact.save()
        messages.success(request, 'Sumited successfully ')
    return render(request , 'contact.html')

def services(request):
    return render(request , 'services.html')
    # return HttpResponse("This is the services page ")