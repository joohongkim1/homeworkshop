from django.shortcuts import render

def info(request):
    return render(request, 'info.html')

def student(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'student.html', context)