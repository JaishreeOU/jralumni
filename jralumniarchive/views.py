from django.shortcuts import render
# from django.utils import timezone
from .models import Student

# Create your views here.
# try


def student_list(request):
    students = Student.objects.order_by('created_date')
#        #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'viewshtmls/student_list.html', {'students': students})
