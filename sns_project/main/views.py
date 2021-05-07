from django.shortcuts import render

def showmain(request):
    return render(request, 'main/mainpage.html')

def showshow(request):
    return render(request, 'main/show.html') 

def first(request):
    return render(request, 'first.html')       

