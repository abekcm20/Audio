from django.urls import path
from . import views

urlpatterns = [
    path('add-song/',views.addsong, name = 'add-song'),
    path('profile/<str:pk>',views.songprofile, name = 'profile-song'),
    path('edit-song/<str:pk>',views.editsong, name = 'edit-son'),
    path('delete-song/<str:pk>',views.deletesong, name = 'delete-song'),
    path('add-podcast/',views.addpodcast, name = 'add-podcast'),
    path('profile/<str:pk>',views.podcastprofile, name = 'profile-podcast'),
    path('edit-podcast/<str:pk>',views.editpodcast, name = 'edit-podcast'),
    path('delete-podcast/<str:pk>',views.deletepodcast, name = 'delete-podcast'),
    path('add-audiobook/',views.addaudiobooks, name = 'add-audiobook'),
    path('profile/<str:pk>',views.audiobookprofile, name = 'profile-audiobook'),
    path('edit-audiobook/<str:pk>',views.editaudiobook, name = 'edit-audiobook'),
    path('delete-audiobook/<str:pk>',views.deleteaudiobook, name = 'delete-audiobook')
]
