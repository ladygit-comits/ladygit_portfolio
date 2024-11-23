from django.shortcuts import render,redirect
from ladygit.models import Contact
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'successful.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')
def contactdit(request):
    return render(request, 'contactdit.html')
def resume(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == 'POST':
        
        contactus = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        contactus.save()

        return redirect('success')
    else:
        return render(request,'contact.html')

@login_required   
def showcontact(request):
        allcontacts = Contact.objects.all()
        return render(request, 'showcontact.html',{'contact':allcontacts})
    
def deletecontact(request,id):
    contact = Contact.objects.get(id = id)
    contact.delete()
    return redirect('showcontact')


