from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):
    lastname = models.CharField(max_length=200, help_text='Enter Last Name')
    firstname = models.CharField(max_length=200, help_text='Enter First Name')
#    alumnifamily = models.ForeignKey('AlumniFamily', on_delete=models.RESTRICT, null=True)
    nickname = models.CharField(max_length=200, help_text='Enter NickName')
    addr1 = models.CharField(max_length=200, help_text='Enter Addr Line 1')
    addr2 = models.CharField(max_length=200, help_text='Enter Addr Line 2')
    city = models.CharField(max_length=200, help_text='Enter Addr City')
    state = models.CharField(max_length=200, help_text='Enter Addr State')
    zip = models.CharField(max_length=10, help_text='Enter Addr Zip')
    birthdate = models.DateField
    phone1 = models.CharField(max_length=100, help_text='Enter Phone')
    emailaddr = models.EmailField(max_length=200, null=True)
#    photo = models.ImageField(upload_to='images/')
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)

    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    verified_date = models.DateTimeField(blank=True, null=True)

    @property
    def lnamefname(self):
        return "%s,- %s" % (self.lastname, self.firstname)

    @property
    def fnamelname(self):
        return "%s %s" % (self.firstname, self.lastname)

    def verify(self):
        self.verified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.lnamefname

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])



class AlumniFamily(models.Model):
    """Model representing a family """
    familyName = models.CharField(max_length=200, help_text='Enter Family Name')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    student = models.ManyToManyField(Student, help_text='Select a student for this family')

    class Meta:
        # …
        permissions = (("can_update", "Can Update Rcord"),)

    def __str__(self):
        """String for representing the Model object."""
        return self.familyName

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this family."""
        return reverse('alumnifamily-detailgc', args=[str(self.id)])
#        return reverse('justsomepage')

    def display_student(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ' and  '.join(student.lnamefname for student in self.student.all()[:3])

# display_student.short_description = 'Kids'

