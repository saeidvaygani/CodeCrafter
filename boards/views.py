from django.http import HttpResponse

def BoardViews(request):
    return HttpResponse('<h1>This is Boards Page for example!</h1>')
