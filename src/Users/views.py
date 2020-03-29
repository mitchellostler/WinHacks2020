from django.shortcuts import render
from .forms import SignUpForm



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

# Create your views here
