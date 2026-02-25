from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Contact   
from .models import Contact   

def home(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                f"Message from {name}",
                message,
                email,
                ["asthasingh2317@gmail.com"],
            )


            Contact.objects.create(
                full_name=name,
                email=email,
                message=message
            )

            form = ContactForm()


    return render(request, "portfolio/home.html", {"form": form})
    return render(request, "portfolio/home.html", {"form": form})

