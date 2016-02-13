from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.utils import timezone

from datetime import datetime

from django.db import models

# Create your models here.
class Person(models.Model):
    pid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_mozillian = models.BooleanField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=10)
    email = models.EmailField()
    want_to_contribute = models.BooleanField()
    TECHNICAL = 'TE'
    NON_TECHNICAL = 'NT'
    BOTH = 'BO'
    NONE = 'NO'
    CONTRIBUTION_CHOICES = (
        (TECHNICAL, 'Technical'),
        (NON_TECHNICAL, 'Non-Technical'),
        (BOTH, 'Both'),
        (NONE, 'None of these')
    )
    contribution_area = models.CharField(max_length=2,
                                        choices=CONTRIBUTION_CHOICES,
                                        default=NONE,
    )
    submitted_on = models.DateTimeField(default=timezone.now)
    query_or_suggestions = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return (self.first_name + ": " + self.email)
