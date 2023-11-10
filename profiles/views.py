from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# profiles/views.py
from django.shortcuts import render, redirect
from .models import Profile
from .form import ProfileEditForm  # Create a form for editing the profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def view_profile(request):
    
    user = request.user
    return render(request, 'profile.html', {'user': user})


@login_required
def edit_profile(request):
    
    # Assuming a one-to-one relationship between User and Profile
    user=request.user
    
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            
            form.save()
            return redirect('view_profile')  # Redirect to the same page after successful form submission
    else:
        form = ProfileEditForm(instance=user)

    return render(request, 'edit_profile.html', {'form': form})
