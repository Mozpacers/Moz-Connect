from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from .forms import RegistrationForm

# Create your views here.

def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                message = "Your Response has been successfully recorded."
            except:
                message = "There was some error saving your data. Please try again later."
            form = RegistrationForm()
    return render_to_response("register.html",
                                locals(),
                                context_instance=RequestContext(request))
