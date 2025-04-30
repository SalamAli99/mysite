from django.shortcuts import render
from django.http import HttpResponse
def students_list(request):
    students=[
        {"name":"salam","age":"25","department":"computer"},
        {"name":"sara","age":"27","department":"econamic"},
        {"name":"somaya","age":"30","department":"computer"},
        {"name":"samar","age":"58","department":"doctor"},
        {"name":"jalal","age":"88","department":"dentist"},

    ]
    
    return HttpResponse(students)