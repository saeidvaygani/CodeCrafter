from django.http import HttpResponse

def StaffsViews(request):
    return HttpResponse('<h1>This is staffs Page for example!</h1>')