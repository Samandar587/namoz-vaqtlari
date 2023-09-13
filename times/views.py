from rest_framework.views import APIView
from .serializers import SalahSerializer, MosqueSerializer, PrayerTimeSerializer
from .models import Salah, Mosque, PrayerTime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def list_salah(request):

    salah_data = Salah.objects.first()
    print(salah_data)

    if not salah_data:
        print('inside salah data')
        salah_data = Salah.objects.create(
            fajr = 'Бомдод',
            dhuhr = 'Пешин',
            asr = 'Аср',
            maghrib = 'Шом',
            isha = 'Хуфтон'
        )

    print('outside salah data')
    print()
    serializer = SalahSerializer(salah_data)
    return Response(serializer.data)

class PrayerTimeView(APIView):
    def post(self, request):
        req_data = request.data
        serializer = PrayerTimeSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        prayer_data = PrayerTime.objects.all()
        serializer = PrayerTimeSerializer(prayer_data, many=True)
        return Response(serializer.data)
