from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from main.views import index, MessageListView, MessageCreateView, MessageUpdateView, MessagDetailView, MessageDeleteView

app_name = 'main'
urlpatterns = [
                  path('', index, name='index'),
                  path('message_list/', MessageListView.as_view(), name='message_list'),
                  path('message_form/', MessageCreateView.as_view(), name='message_create'),
                  path('message_form/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
                  path('message_detail/<int:pk>/', MessagDetailView.as_view(), name='message_detail'),
                  path('message_delete/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
              ] + staticfiles_urlpatterns()
