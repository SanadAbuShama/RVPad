import re
from django.shortcuts import redirect, render
from login_registration_app.models import User
from rvpad_app.models import Restaurant, Review

# FOR REVIEW


def restaurant_details(request, rest_id):
    rest = Restaurant.objects.get(id=rest_id)
    reviews = rest.reviews.all()
    sum = 0
    for review in reviews:
        sum = sum+int(review.rating)
    if len(reviews) > 0:
        rating = sum/len(reviews)
    else:
        rating = 'No ratings yet'
    context = {
        'rest': rest,
        'rating': rating
    }
    return render(request, 'rest_details.html', context)


def add_restaurant(request):
    return render(request, 'add_rest.html')


def create_restaurant(request):
    if 'userid' in request.session:
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
