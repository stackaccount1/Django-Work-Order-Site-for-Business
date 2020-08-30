from django.db import models
import datetime
from django.urls import reverse
from django.conf import settings

class Workorder(models.Model):
    addressnumber = models.DecimalField(max_digits=10, decimal_places=0)
    addressstreet = models.CharField(max_length=60)
    addresstown = models.CharField(max_length=60)
    addressstate = models.CharField(max_length=60)
    quickdescrip = models.CharField(max_length=350)
    lockboxcode = models.CharField(max_length=25)
    description = models.CharField(max_length=300)
    proposalorestimatenumber = models.DecimalField(max_digits=15, decimal_places=0)
    clientemailinfo = models.CharField(max_length=400)
    techniciancompletionnotes = models.CharField(max_length=500)
    taskdatecomplete = models.DateField(("Date"), default=datetime.date.today)
    taskdatestart = models.DateField(("Date"), default=datetime.date.today)
    taskcomplete = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    invoicesent = models.BooleanField(default=False)
    client = models.CharField(max_length=25)

    def __str__(self):
        return self.addressnumber + self.addressstreet + self.quickdescrip + self.lockboxcode + self.client

    def get_absolute_url(self):
        return reverse('wordorderapp:detail', kwargs={'pk': self.pk})

class Dailyjournal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    journaldate = models.DateField(("Date"), default=datetime.date.today)
    description = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('wordorderapp:home1')
