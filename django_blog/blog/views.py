from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserEditForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile view after saving changes
    else:
        form = UserEditForm(instance=request.user)
    
    return render(request, 'blog/edit_profile.html', {'form': form})
