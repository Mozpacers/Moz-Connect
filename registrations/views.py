from django.shortcuts import render_to_response, RequestContext
from django.http import JsonResponse
from .forms import RegistrationForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def register(request):
    '''
    View to render registration form
    '''
    form = RegistrationForm(None)
    return render_to_response("register.html",
                              locals(),
                              context_instance=RequestContext(request)
    )


@csrf_exempt
def save_registeration_form(request):
    '''
    View to save registration form via AJAX call
    '''
    if request.is_ajax():
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            message = "Success"
            return JsonResponse({"message": message})
        else:
            message = "Fail"
            data = {'message': message}
            # Un-comment if form.errors to be passed via AJAX
            # to front-end
            '''
            data = {'message': message,
                    'errors': dict(
                        [(k, [unicode(e) for e in v]
                        ) for k,v in form.errors.items()]
                    )
            }
            '''
            return JsonResponse(data)
