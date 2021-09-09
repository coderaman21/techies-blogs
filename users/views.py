from django.shortcuts import render , redirect
from django.contrib import messages
from .form import userregisterform,userupdateform,profileupdateform
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = userregisterform(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Account created for {username} , login to your account')
            return redirect('login')
    else:        
        form = userregisterform()
    return render(request,'users/signup.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = userupdateform(request.POST,instance=request.user)
        p_form = profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Account info has been updated succesfully. ')
            return redirect('profile')
    else:
        u_form = userupdateform(instance=request.user)
        p_form = profileupdateform(instance=request.user.profile)
    
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    } 

    return render(request,'users/profile.html',context)