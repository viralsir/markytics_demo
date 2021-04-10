from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class newincident(models.Model):
    location=models.CharField(max_length=45,choices=[('Coroprate Headoffice','Coroprate Headoffice'),
                                                     ('Operations Department','Operations Department'),
                                                     ('Wrok Station','Wrok Station'),
                                                     ('Marketing Division','Marketing Division')],
                                                    verbose_name="Location")

    incident_department=models.TextField(verbose_name="Incident Department :")
    date_incident=models.DateTimeField(verbose_name='Date and Time of Incident')
    incident_location=models.TextField(verbose_name='Incident Location')
    initial_serverity=models.TextField(max_length=55,choices=[('Mild','Mild'),('Modarate','Modarate'),('Severe','Severe'),('Fatal','Fatal')])
    action_tacken=models.TextField(verbose_name='Immediate Action Taken :')
    sub_type=models.CharField(max_length=55,choices=[('Enviourmental Incident','Enviourmental Incident'),
                                                     ('Injury/illness','Injury/illness'),
                                                     ('Property Demage','Property Demage'),
                                                     ('Vehicle','Vehicle')])

    user=models.OneToOneField(User,models.CASCADE,related_name='incident')

    def get_absolute_url(self):
        return reverse('home')