import re
from django.shortcuts import redirect, render
from login_registration_app.models import User
from rvpad_app.models import Restaurant, Review

# FOR REVIEW


def restaurant_details(request, rest_id):
    rest = Restaurant.objects.get(id=rest_id)
    """ reviews = rest.reviews.all()
    sum = 0
    for review in reviews:
        sum = sum+int(review.rating)
    rating = sum/len(reviews) """
    context = {
        'rest': rest,
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
        return redirect('/')


def about_us(request):
    return render(request, 'about_us.html')


def landing_page(request):
    return render(request, 'landing.html')
