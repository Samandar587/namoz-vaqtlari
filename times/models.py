from django.db import models

class Mosque(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Salah(models.Model):
    fajr = models.CharField(max_length=50)
    dhuhr = models.CharField(max_length=50)
    asr = models.CharField(max_length=50)
    maghrib = models.CharField(max_length=50)
    isha = models.CharField(max_length=50)
    
class PrayerTime(models.Model):
    mosque = models.ForeignKey(Mosque, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    fajr_time = models.TimeField()
    dhuhr_time = models.TimeField()
    asr_time = models.TimeField()
    maghrib_time = models.TimeField()
    isha_time = models.TimeField()
