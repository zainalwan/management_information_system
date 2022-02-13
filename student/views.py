from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from .models import Student
import json

# Create your views here.
def index(request):
    if request.method == 'GET':
        students = Student.objects.all()
        if students.exists():
            return JsonResponse({
                'students': list(students.values()),
                'status': True
            })
        else:
            return JsonResponse({
                'status': True,
                'message': 'The student doesn\'t exixst'
            })
    else:
        return JsonResponse({'status': False}, status = 404)

def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            Student.objects.create(
                name = data['name'],
                major = data['major'],
                email = data['email'],
            )
            return JsonResponse({'status': True})
        except IntegrityError:
            return JsonResponse({
                'status': True,
                'message': 'Email has been registered.'
            })
    else:
        return JsonResponse({'status': False}, status = 404)

def detailUpdateDelete(request, id):
    if request.method == 'GET' or request.method == 'PUT' \
        or request.method == 'DELETE':
        student = Student.objects.filter(id = id)
        if student.exists():
            if request.method == 'GET':
                return detail(student)
            elif request.method == 'PUT':
                return update(student, json.loads(request.body))
            elif request.method == 'DELETE':
                return delete(student)
        else:
            return JsonResponse({
                'status': True,
                'message': 'The student doesn\'t exixst'
            })
    else:
        return JsonResponse({'status': False}, status = 404)

def detail(student):
    return JsonResponse({
        'student': student.values()[0],
        'status': True
    })

def update(student, data):
    student.update(
        name = data['name'],
        major = data['major'],
        email = data['email'],
    )
    return JsonResponse({'status': True})

def delete(student):
    student.delete()
    return JsonResponse({'status': True})