from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def view_home(request):
    """
    Function enables user to view the home page.
    """
    return render(request, 'index.html')


def view_services(request):
    """
    Function enables user to view the services page.
    """
    return render(request, 'services.html')


def contact(request):
    """
    Function enables user to view the contact page.
    """
    return render(request, 'contact.html')


def view_about(request):
    """
    Function enables user to view the about page.
    """
    return render(request, 'about.html')


def view_blog(request):
    """
    Function enables user to view the blog page.
    """
    return render(request, 'blog.html')    


def handler404(request, *args, **argv):
    """
    Function to enable customizing 404 error
    page in production environment if booking is not found.
    """
    form = BookingForm()
    context = {
        'form': form
        }
    response = render(request, 'not_found.html', context)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    """
    Function to enable customizing 404 error page
    in production environment if booking is duplicate.
    """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    response = render(request, 'duplicate_booking.html', context)
    response.status_code = 500
    return response


@login_required
def add_booking(request):
    """
    Function enables user to make a booking
    and add it to the database.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful.')
            return redirect('view_booking')
        else:
            messages.error(request, 'Booking date must be in the future.')
    form = BookingForm()
    context = {
        'form': form
        }
    return render(request, 'add_booking.html', context)


@login_required
def view_booking(request):
    """
    Function enables user to view a booking after
    it has been made and added to the database.
    """
    bookings = Booking.objects.filter(user__in=[request.user])
    context = {
        'bookings': bookings
    }
    return render(request, 'view_booking.html', context)


@login_required
def edit_booking(request, booking_id):
    book = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been updated.')
        return redirect('view_booking')
    form = BookingForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    """
    Function enables user to delete a booking after
    it has been made and added to the database.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if booking.delete():
            messages.success(request, 'Your booking has been deleted.')
            return redirect('view_booking')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'delete_booking.html', context)



