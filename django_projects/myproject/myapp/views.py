from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, FeedbackForm
from .models import Feedback
from django.shortcuts import get_object_or_404

def home(request):
    # return HttpResponse("<h1>Hello this is home page")
    return render(request, "myapp/home.html")

def about(request):
    # return HttpResponse("<h1>Hello this is home page")
    return render(request, "myapp/about.html")

def contact(request):
    # return HttpResponse("<h1>Hello this is home page")
    return render(request, "myapp/contact.html")

def login(request):
    return render(request,"myapp/login.html")

def register(request):
    return render(request,"myapp/register.html")

def contact_view(request):
    form=ContactForm()

    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            print(name, email, message)
            return render(request,"myapp/thankyou.html")
    return render(request, 'myapp/contact.html',{'form':form})

def feedback_view(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"myapp/thankyou.html")
    else:
        form=FeedbackForm()


    return render(request,"myapp/feedback.html",{'form':form})

def show_feedback(request):
    feedbacks=Feedback.objects.all()
    return render(request,"myapp/show_feedback.html",{"feedbacks ":feedbacks})

def delete_feedback(request, feedback_id):
    feedback=get_object_or_404(Feedback, id=feedback_id)
    feedback.delete()
    return redirect("show_feedback")

def edit_feedback(request, feedback_id):
    feedback=get_object_or_404(request, id=feedback_id)