from django.urls import path

from .views import (home, login_page, signup_page, register,
                    user_page, user_login, reservation_page, contact_page, search_rooms, refresh_rooms,
                    book_room,booking_page, cancel_reservation,password_page,change_password)
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', home, name='home'),
    path('login_page/', login_page, name='login_page'),
    path('signup_page/', signup_page, name='signup_page'),
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
    path('user_page/', user_page, name='user_page'),
    path('reservation_page/',reservation_page,name='reservation_page'),
    path('contact_page/', contact_page, name='contact_page'),
    path('search/', search_rooms, name='search_rooms'),
    path('refresh_rooms/', refresh_rooms, name='refresh_rooms'),
    path('book_room/', book_room, name='book_room'),
    path('booking_page/<str:room_name>/', booking_page, name='booking_page'),
    path('cancel_reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    path('password_page/', password_page, name='password_page'),
    path('change_password/', change_password, name='change_password'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)