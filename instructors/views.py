from django.http import HttpResponse

def InstructorsViews(request):
    return HttpResponse('<h1>This is Instructors Page for example!</h1>')