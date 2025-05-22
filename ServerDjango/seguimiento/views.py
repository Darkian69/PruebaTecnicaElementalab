from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse

URL = {
    "1" : "https://elementalab.com/",
    "2": "https://www.utp.edu.co",
    "3": "https://www.google.com"
}

def tracking_url(request: HttpRequest):
    mail = request.GET.get("u")
    web_clic = request.GET.get("t")

    link = URL.get(web_clic)
    print(f"{mail} - {link}")

    return redirect(link)