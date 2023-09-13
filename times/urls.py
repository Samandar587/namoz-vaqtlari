from django.urls import path
from .views import list_salah, PrayerTimeView

urlpatterns = [
    path("list-salahs", list_salah),
    path("prayer-times", PrayerTimeView.as_view())
]