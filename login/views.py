from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from general_functions import error_message
from .forms import CustomUserCreationForm
from petPosts.models import PetPost

# Create your views here.


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html', {'user_form': CustomUserCreationForm,
                                             'pet_posts': PetPost.objects.all()})
    
    def post(self, request):
        if 'btn_login' in request.POST:
            user = request.POST.get('inp_username')
            password = request.POST.get('inp_password')
            auth_user = authenticate(request, username=user, password=password)
            if not auth_user:
                auth_user = authenticate(request, email=user, password=password)
            if auth_user:
                login(request, auth_user)
                error = None
            else:
                error_message(request, 'Usuario/Email o Contraseña incorrectos.')
                error = 'login'
            return render(request, 'home.html', {'user_form': CustomUserCreationForm,
                                                 'error': error,
                                                 'pet_posts': PetPost.objects.all()})
        else:
            user_form = CustomUserCreationForm(request.POST)
            if user_form.is_valid():
                new_user = user_form.save()
                auth_user = authenticate(request, username=new_user.username, password=new_user.password)
                if not auth_user:
                    auth_user = authenticate(request, email=user, password=password)
                if auth_user:
                    login(request, auth_user)
                    error = None
                else:
                    error_message(request, 'Usuario/Email o Contraseña incorrectos.')
                    error = 'login'
                return render(request, 'home.html', {'user_form': CustomUserCreationForm,
                                                     'error': error,
                                                     'pet_posts': PetPost.objects.all()})
            else:
                return render(request, 'home.html', {'user_form': user_form,
                                                     'error': 'new_user',
                                                     'pet_posts': PetPost.objects.all()})



def logout_view(request):
    logout(request)
    response = redirect('home')
    response.delete_cookie('sessionid')
    return response
