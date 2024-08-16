from django.urls import path

from joatssapp.views import JoatssView

urlpatterns = [
    path('joatss', JoatssView.as_view()),
]
