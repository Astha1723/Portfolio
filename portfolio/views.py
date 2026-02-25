from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
<<<<<<< HEAD
from .models import Contact   # ✅ ADD THIS
=======
from .models import Contact   
>>>>>>> 0acc1b6f495685600b34ac4a7f53f90d0435f851

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

<<<<<<< HEAD
            # ✅ SAVE TO DATABASE
=======
    
>>>>>>> 0acc1b6f495685600b34ac4a7f53f90d0435f851
            Contact.objects.create(
                full_name=name,
                email=email,
                message=message
            )

            form = ContactForm()

<<<<<<< HEAD
    return render(request, "portfolio/home.html", {"form": form})
=======
    return render(request, "portfolio/home.html", {"form": form})
>>>>>>> 0acc1b6f495685600b34ac4a7f53f90d0435f851
