from django.shortcuts import render
from rest_framework import generics

from django.http import JsonResponse
from django.db import connection

from .models import CB_Driver_Master
from user.models import CB_Trans_Table
from .serializers import DriverSerializer, TransSerializer


from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    return render(request, 'login.html')


def totalKMDetails(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT SUM(TotalKmTravelled) from maladb.CB_Trans_Table;")
            totalKM = cursor.fetchone()

            for r in totalKM:
                print(r)
                context = {'totalKM':r}
                return JsonResponse(context)

def bookingMonthDetails(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from maladb.CB_Trans_Table where MONTH(dt) = MONTH(CURRENT_DATE());")
            currentMonth = cursor.fetchall()
            print(currentMonth)

            # for r in currentMonth:
            #     print(r)
            #     context = {'currentMonth':r}
            return JsonResponse(currentMonth)



class DriverList(generics.ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = CB_Driver_Master.objects.all()

class BookingList(generics.ListCreateAPIView):
    serializer_class = TransSerializer
    queryset = CB_Trans_Table.objects.all()

class BookingSearchList(generics.ListAPIView):    
    serializer_class = TransSerializer
    lookup_url_kwarg = "dt"

    def get_queryset(self):
        dt = self.kwargs.get(self.lookup_url_kwarg)
        dateSearch = CB_Trans_Table.objects.filter(dt=dt)
        return dateSearch

# class BookingList(generics.ListCreateAPIView):
#     serializer_class = TransSerializer

#     Time_From = request.POST['Time_From']
#     queryset = CB_Trans_Table.objects.all()

# class PrdocutList(APIView):
#       def post(self, request, format=None):
#         query = request.data.get('query')
#         if query:
#             products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains = query))
#         else:
#             products =  Product.objects.none()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)




# class DriverList(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = DriverSerializer
#     queryset = CB_Driver_Master.objects.all()
        
