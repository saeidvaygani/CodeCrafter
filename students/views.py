from django.http import HttpResponse 

def StudentsViews(request):
    return HttpResponse('<h1>This is Students Page for example!</h1>')