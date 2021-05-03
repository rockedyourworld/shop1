from django.urls import path

from pages.views import ContactView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact')
]
