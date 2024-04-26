

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Room

from django.http import HttpResponseForbidden
from .models import Reservation
from datetime import datetime
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages












def home(request):
    return render(request, 'home_page.html')


def login_page(request):
    return render(request, 'login_page.html')


# myapp/views.py
from .forms import CreateUserForm

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')

    error_message = 'Signup Failed'
    return render(request, 'signup_page.html', {'error_message': error_message})


def signup_page(request):
    return render(request, 'signup_page.html')

@login_required
def user_page(request):
    rooms = Room.objects.all()

    return render(request, 'user_page.html', {'rooms': rooms})





def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('user_page')
        else:

            error_message = 'Invalid login credentials'
            return render(request, 'login_page.html', {'error_message': error_message})

    return render(request, 'login_page.html')


def reservation_page(request):
    user_reservations = Reservation.objects.filter(guest=request.user)
    context = {'user_reservations': user_reservations}

    return render(request, 'reservation_page.html', context)

def contact_page(request):
    return render(request, 'contact_page.html')


def search_rooms(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        arrive_date = request.POST.get('arrive_date')
        departure_date = request.POST.get('departure_date')
        beds = request.POST.get('beds')

        rooms = Room.objects.filter(
            location__city=city,
            available_from__lte=arrive_date,
            available_to__gte=departure_date,
            beds__gte=beds,
            status="available"



        )


        return render(request, 'user_page.html', {'rooms': rooms})
    else:
        return render(request, 'user_page.html', {'rooms': Room.objects.all()})

def refresh_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'user_page.html', {'rooms': rooms})




def booking_page(request, room_name):
    return render(request, 'booking_page.html', {'room_name': room_name})


@login_required
def book_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        user = request.user


        check_in_str = request.POST.get('check_in')
        check_out_str = request.POST.get('check_out')

        # Convert date strings to datetime objects
        check_in = datetime.fromisoformat(check_in_str)
        check_out = datetime.fromisoformat(check_out_str)

        name = request.POST.get('name')
        surname = request.POST.get('surname')

        mail = request.POST.get('mail')

        room = get_object_or_404(Room, name=room_name)


        # Utwórz obiekt Reservation
        reservation = Reservation.objects.create(
            guest=user,
            room=room,
            check_in=check_in,
            check_out=check_out,
            name=name,
            surname=surname,
            mail=mail

        )
        reservation.save()

        room.status="not available"
        room.save()
        return redirect('reservation_page')


    return redirect('contact_page')


@login_required
def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    reservation.room.status = "available"
    reservation.room.save()
    if request.user == reservation.guest:
        reservation.delete()

        return redirect('reservation_page')
    else:
        return HttpResponseForbidden("You don't have permission to cancel this reservation.")


def password_page(request):
    return render(request, 'password_page.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()

            update_session_auth_hash(request, user)
            messages.success(request, 'Hasło zostało pomyślnie zmienione.')
            return redirect('user_page')
        else:
            messages.error(request, 'Proszę poprawić błędy w formularzu.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'password_page.html', {'form': form})


