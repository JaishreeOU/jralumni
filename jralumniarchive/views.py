from django.shortcuts import render
# from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Student, AlumniFamily
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required


# Create your views here.
# try

####################
# Function Based View
####################
def dashboard(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_families = AlumniFamily.objects.all().count()
    num_students = Student.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Set session as modified to force data updates/cookie to be saved.
    request.session.modified = True

    context = {
        'num_families': num_families,
        'num_students': num_students,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variablesssss
    return render(request, 'viewshtmls/dashboard.html', context=context)


@login_required
def justsomepage(request):
    """View function for justsomepage."""
    cities = [
        {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
        {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
        {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
        {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
        {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
    ]

    context = {
        'message': 'Landing here',
        'cities': cities
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'viewshtmls/justsomepage.html', context=context)



@login_required
def student_list(request):
    students = Student.objects.order_by('created_date')
#        #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'viewshtmls/student_list.html', {'students': students, 'additional_data': 'This is from student_list'})



@login_required
def family_list(request):
    alumnifamily_list = AlumniFamily.objects.all()
#        #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'viewshtmls/alumnifamily_list.html', {'alumnifamily_list': alumnifamily_list, 'additional_data': 'This is from family_list'})


@login_required
def family_detail_view(request, primary_key):
    additional_data = request.GET.get('additional_data') + '-> family_detail_view'

    try:
        alumnifamily = AlumniFamily.objects.get(id=primary_key)
    except AlumniFamily.DoesNotExist:
        raise Http404('AlumniFamily does not exist')
#    alumnifamily = get_object_or_404(AlumniFamily, pk=primary_key)
    return render(request, 'viewshtmls/alumnifamily_detail.html', context={'alumnifamily': alumnifamily, 'additional_data': additional_data} )

###################
# generic Class Based View
###################
class FamilyListView(LoginRequiredMixin,ListView):
    model = AlumniFamily
    template_name = "viewshtmls/alumnifamily_list.html"
    paginate_by = 2
#    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return AlumniFamily.objects.all()
#       filter(familyName__icontains='a')[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(FamilyListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['additional_data'] = 'This is from FamilyListView'
        return context


class AlumniFamilyByUserListView(LoginRequiredMixin,ListView):
    """Generic class-based view listing books on loan to current user."""
    model = AlumniFamily
    template_name = 'viewshtmls/alumnifamilybyuser_list.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            AlumniFamily.objects.filter(familyName=self.request.user)
        )



class StudentListView(LoginRequiredMixin,ListView):
    model = Student
    template_name = "viewshtmls/student_list.html"
    context_object_name = "students"
    paginate_by = 2
#    login_url = '/login/'
    redirect_field_name = 'next'

    def get_queryset(self):
        """Return the last five published questions."""
        return Student.objects.order_by("-lastname")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(StudentListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['additional_data'] = 'This is from StudentListView'
        return context


class FamilyDetailView(LoginRequiredMixin,DetailView):
    model = AlumniFamily
    template_name = "viewshtmls/alumnifamily_detail.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(FamilyDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
#        context['additional_data'] = 'This is from StudentListView'
        return context