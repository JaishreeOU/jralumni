

from django.urls import path
from . import views

app_name = "jralumniarchive"

urlpatterns = [
    path('', views.student_list, name='student_list'),
#    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
