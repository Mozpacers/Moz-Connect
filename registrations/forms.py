from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Person

class RegistrationForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ('submitted_on',)
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'is_mozillian': _('I\'m a Mozillian'),
            'phone_number': _('Phone Number'),
            'email': _('Email Address'),
            'want_to_contribute': _('I want to contribute to Mozilla'),
            'contribution_area': _('I would like to contribute to'),
            'query_or_suggestions': _('Please let us know if you have any queries/suggestions'),
        }
