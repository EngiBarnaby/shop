from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username = cd['username'], password = cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse("Вы успешно вошли")
#                 else:
#                     return HttpResponse("Акаунт заблокирован")
#             else:
#                 return HttpResponse('Неверно указаны имя или пароль')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form' : form})

@login_required
def dashboard(request):
    return render(request, 'account/index.html', {'section' : 'dashboard'})


def user_profil(request, username):
    user = User.objects.get(username=request.user)
    context = {'user' : user}
    return render(request, 'account/profil.html', context)


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user' : new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registration.html', {'user_form': user_form})
