from django.conf import settings
from django.db import models
from django.utils import timezone


class Student(models.Model):
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    addr1 = models.CharField(max_length=200)
    addr2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=10)
    birthdate = models.DateField
    phone1 = models.CharField(max_length=100)
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
