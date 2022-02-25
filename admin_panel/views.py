
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login


def reload():
    return HttpResponse(
        """<title>Processing...</title><script>
        window.location = window.location.pathname;
        </script>"""
    )


# Create your views here.
def admin_login_view(request, *args, **kwargs):
    pass


def admin_panel_view(request, *args, **kwargs):
    context = {}

    if request.method == 'POST':

        try:
            username = request.POST['new-username']
            password = request.POST['new-password']
        except: # if the fiels are invalid
            return reload()
        
        print(f'USERNAME: {username} PASSWORD: {password}')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

        return reload()

    if not request.user.is_authenticated:
        response = render(request, 'login.html', context)
        return response

    from api.models import Type, Color, Collection

    colors = []
    types = []
    collections = []


    for i in Color.objects.all():
        colors.append(model_to_dict(i))
    for i in Type.objects.all():
        types.append(model_to_dict(i))
    for i in Collection.objects.all():
        collections.append(model_to_dict(i))
    


    # print(colors, types, collections)


    context = {
        'colors': colors,
        'types': types,
        'collections': collections,
    }

    response = render(request, 'admin_panel.html', context)

    return response