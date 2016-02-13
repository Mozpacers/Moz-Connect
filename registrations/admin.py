from django.contrib import admin
from .models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    # list_display = Person._meta.get_all_field_names()
    list_display = ('pid', 'first_name', 'last_name', 'phone_number', 'email',
                    'is_mozillian', 'want_to_contribute', 'contribution_area',
                    'submitted_on', 'query_or_suggestions')

admin.site.register(Person, PersonAdmin)
