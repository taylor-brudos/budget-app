from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "first_app/index.html")

def myaccounts(request):
    return render(request, "first_app/my_accounts.html")
    
def show(request):
    return render(request, "first_app/account_detail.html")
