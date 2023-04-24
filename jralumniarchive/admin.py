from django.contrib import admin

from .models import Student,AlumniFamily


# Define the admin class
class StudentAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'addr1', 'addr2')
    fields = [('lastname', 'firstname'), ('addr1',  'addr2', 'city','state','zip')]

class AlumniFamilyAdmin(admin.ModelAdmin):
    list_display = ('familyName', 'display_student')


# Register your models here.
# admin.site.register(Student)
# admin.site.register(AlumniFamily)

admin.site.register(Student,StudentAdmin)
admin.site.register(AlumniFamily,AlumniFamilyAdmin)