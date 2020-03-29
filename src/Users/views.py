from django.shortcuts import render
from .forms import SignUpForm, LoginForm
from .models import Login, MyUser
from  django.http import QueryDict
from django.http import HttpResponseRedirect


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    validated = False
    nameex = False
    if request.method == 'POST':
        inUser = request.POST.__getitem__('username')
        inPass = request.POST.__getitem__('password')
        form = Login(request.POST)
        try:
            user = MyUser.objects.get(username=inUser)
            nameex = True
        except:
            print('NONE')
        if nameex:
            if user.password == inPass:
                validated = True
        if validated:
            print('PASSED')
            return HttpResponseRedirect('login')
        else:
            print('Failed')
    form = LoginForm(request.POST)
    return render(request, 'login.html', {'form': form})

# Create your views here
