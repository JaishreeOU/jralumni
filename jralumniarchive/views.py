from django.shortcuts import render
# from django.utils import timezone
from .models import Student
from django.views import generic

# Create your views here.
# try


def student_list(request):
    students = Student.objects.order_by('created_date')
#        #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'viewshtmls/student_list.html', {'students': students})


class IndexView(generic.ListView):
    model = Student
    template_name = "jralumniarchive/student_list.html"
    context_object_name = "student_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]