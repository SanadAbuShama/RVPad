from multiprocessing import context
import re
from django.shortcuts import redirect, render
from login_registration_app.models import User
from rvpad_app.models import Restaurant, Review
from django.contrib import messages


def restaurant_details(request, rest_id):
    if 'userid' in request.session:
        rest = Restaurant.objects.get(id=rest_id)
        reviews = rest.reviews.all()
        sum = 0
        for review in reviews:
            sum = sum+int(review.rating)
        if len(reviews) > 0:
            rating = round(sum/len(reviews), 1)
        else:
            rating = 'No ratings yet'
        context = {
            'rest': rest,
            'rating': rating
        }
        return render(request, 'rest_details.html', context)
    else:
        return redirect('/login_register')


def add_restaurant(request):
    if 'userid' in request.session:
        return render(request, 'add_rest.html')
    else:
        return redirect('/login_register')


def create_restaurant(request):
    if 'userid' in request.session:
        errors = Restaurant.objects.restaurant_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/rvpad/restaurants/new')
        else:
            logged_user = User.objects.get(id=request.session['userid'])
            created_rest = Restaurant.objects.create(
                name=request.POST['name'], description=request.POST['desc'], location=request.POST['location'], posted_by=logged_user)
            if 'image' in request.FILES:
                created_rest.image = request.FILES['image']
                created_rest.save()
            return redirect('/rvpad/restaurants')
    else:
        return redirect('/login_register')


def about_us(request):
    return render(request, 'about_us.html')


def landing_page(request):
    return render(request, 'landing.html')


def restaurants(request):
    if 'userid' in request.session:
        context = {
            'rests': Restaurant.objects.all()
        }
        return render(request, 'home.html', context)
    else:
        redirect('/login_register')


def add_review(request, rest_id):
    if 'userid' in request.session:
        logged_user = User.objects.get(id=request.session['userid'])
        rest = Restaurant.objects.get(id=rest_id)
        Review.objects.create(
            text=request.POST['rev_text'], rating=request.POST['rating'], posted_by=logged_user, reviewed_restaurant=rest)

        return redirect(f'/rvpad/restaurants/{rest_id}')
    else:
        return redirect('/login_register')


def user_profile(request, user_id):
    if 'userid' in request.session:
        user = User.objects.get(id=user_id)
        reviews = user.reviews.all()
        context = {
            'user': user,
            'num_reviews': len(reviews)
        }
        return render(request, 'user_prof.html', context)
    else:
        return redirect('/login_register')


def restaurant_delete(request, rest_id):
    if 'userid' in request.session:

        rest = Restaurant.objects.get(id=rest_id)
        rest.delete()
        return redirect('/rvpad/restaurants')
    else:
        return redirect('/login_register')


def review_delete(request, rev_id, rest_id):
    if 'userid' in request.session:
        rev = Review.objects.get(id=rev_id)
        rev.delete()
        return redirect(f'/rvpad/restaurants/{rest_id}')
    else:
        return redirect('/login_register')


def edit_restaurant(request, rest_id):
    if 'userid' in request.session:
        context = {
            'rest': Restaurant.objects.get(id=rest_id)
        }
        return render(request, 'edit_rest.html', context)
    else:
        return redirect('/login_register')


def update_restaurant(request, rest_id):
    if 'userid' in request.session:
        errors = Restaurant.objects.restaurant_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/rvpad/restaurants/edit/{rest_id}')
        else:
            rest = Restaurant.objects.get(id=rest_id)
            rest.name = request.POST['name']
            rest.description = request.POST['desc']
            rest.location = request.POST['location']
            if 'image' in request.FILES:
                rest.image = request.FILES['image']
            rest.save()

            return redirect(f'/rvpad/restaurants/{rest_id}')
    else:
        return redirect('/login_register')
