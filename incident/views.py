from django.shortcuts import render
from django.views.generic import CreateView
from .models import newincident
# Create your views here.
class NewIncidentView(CreateView):
    model = newincident
    fields = '__all__'


    def get_form(self, form_class=None):
       form = super(NewIncidentView, self).get_form(form_class)
       form.fields['date_incident'].widget.attrs.update({'class': 'datepicker'})
       return form
