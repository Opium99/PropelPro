from django.shortcuts import render

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm


# Create your views here.
def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            print("Sorry! this email already exists")
        else:
            instance.save()

    context = {
        'form': form,
    }
    template = "newsletters/templates/sign_up.html"
    return render(request, "sign_up.html", context)

def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exist():
            NewsletterUser.objects.filter(email=instance.email).delete()
        else:
            print("Sorry but we did not find your email address")
    context = {
        "form": form,
    }
    template = "newsletters/templates/unsubscribe.html"
    return render(request, "unsubscribe.html", context)

def about(request):
         template= "newsletters/tempaltes/about.html"
         return render(request, "about.html",)
