from django.shortcuts import render


def base(request, name):
    return render(request, 'app/home.html', {'name': name})
