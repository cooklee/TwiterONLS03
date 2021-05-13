from django.urls import path
from twitter import views

urlpatterns = [
    path('add_tweet/', views.AddTweetView.as_view(), name='add_tweet'),
    path('add_message/', views.AddMessageView.as_view(), name='add_message'),
    path('update_tweet/<int:pk>/', views.UpdateTweetView.as_view(), name='update_tweet'),
    path('message_list/', views.ShowMessagesView.as_view(), name='message_list'),
]
