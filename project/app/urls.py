from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('home', views.home),
    path('list', views.list),
    path('reg', views.reg),
    path('form', views.form),
    path('login', views.login),
    path('', views.index),
    path('hotel', views.hotel),
    path('log', views.login),
    path('miniproject', views.home),
    path('imageupload', views.imageupload),
    path('display', views.display),
    path('upd', views.upd),
    path('delete<int:id>', views.delete),
    path('display/', views.display),
    path('display/display', views.display),
    path('editdata<int:id>', views.editdata),
    path('edit/<int:id>', views.edit),
    path('delete/', views.delete, name='delete'),
    path('hotel_search/', views.hotel_search, name='hotel_search'),
    path('generate_itinerary/', views.generate_itinerary, name='generate_itinerary'),
    path('reviews/', views.reviews_view, name='reviews'),  # URL to the review page
    path('index2/', views.index2, name='index2'),
    path('plan-itinerary/', views.plan_itinerary, name='plan_itinerary'),
    path('comments/', views.comment_view, name='comments'),
    path('comments/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comments/reply/<int:comment_id>/', views.reply_comment, name='reply_comment'),
    path('chat/', views.chat_view, name='chat'),
    path('chat/delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('rental_form/', views.rental_form, name='rental_form'),
    path('submit-form/', views.rental_form, name='submit_form'),
]















