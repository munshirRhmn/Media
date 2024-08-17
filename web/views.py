from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import User
import uuid
from django.utils.text import slugify

def index(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Hash the password before saving
        hashed_password = make_password(password)

        # Generate a unique slug
        slug = slugify(username) + '-' + str(uuid.uuid4())[:8]  # Example: john-doe-1a2b3c4d

        # Save the user to the database
        user_save = User(
            username=username,
            email=email,
            password=hashed_password,
            slug=slug
        )
        user_save.save()

        messages.success(request, 'User added successfully!')
        return redirect('web:result_show')

    return render(request, "web/index.html")


def result_show(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'web/result_show.html', context)


def edit(request, slug):
    user = get_object_or_404(User, slug=slug)

    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')

        if username and email:
            user.username = username
            user.email = email
            user.save()
            messages.success(request, 'User updated successfully!')
            return redirect('web:result_show')  # Ensure this URL pattern exists

    return render(request, 'web/edit.html', {'user': user})



def delete(request, slug):
    user = get_object_or_404(User, slug=slug)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('web:result_show')
    return render(request, 'web/delete.html', {'user': user})

