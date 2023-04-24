from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Student(models.Model):
    lastname = models.CharField(max_length=200, help_text='Enter Last Name')
    firstname = models.CharField(max_length=200, help_text='Enter First Name')
    nickname = models.CharField(max_length=200, help_text='Enter NickName')
    addr1 = models.CharField(max_length=200, help_text='Enter Addr Line 1')
    addr2 = models.CharField(max_length=200, help_text='Enter Addr Line 2')
    city = models.CharField(max_length=200, help_text='Enter Addr City')
    state = models.CharField(max_length=200, help_text='Enter Addr State')
    zip = models.CharField(max_length=10,help_text='Enter Addr Zip')
    birthdate = models.DateField(help_text='Enter Date of Birth')
    phone1 = models.CharField(max_length=100, help_text='Enter Phone')
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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

