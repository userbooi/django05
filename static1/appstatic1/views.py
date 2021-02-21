from django.shortcuts import render

# Create your views here.
def home(requests):
    info = {'key':' (hey, another project of the webpage)'}
    return render(requests, 'index.html', info)