from django.shortcuts import render
from .forms import Send_email
# Create your views here.
from django.core.mail import send_mail


def contact(request):
    if request.POST:
        send_mail(
            f'{request.POST["Subject"]} -> {request.POST["name"]} : {request.POST["email"]}',
            f'{request.POST["name"]},{request.POST["email"]},{request.POST["Subject"]}\n {request.POST["message"]}',
            'obidzeromax@gmail.com',
            [f'{request.POST["email"]}'],
            fail_silently=False,
        )
    form = Send_email()
    ctx = {
        "form": form
    }
    return render(request, "contact/contact.html", ctx)


def page_404(request):
    return render(request, "pages/404.html", {})


def page_faq(request):
    return render(request, "pages/faq.html", {})


def page_about(request):
    return render(request, "pages/about.html", {})


def page_services(request):
    return render(request, "pages/services.html", {})


def page_pricing(request):
    return render(request, "pages/pricing.html", {})
