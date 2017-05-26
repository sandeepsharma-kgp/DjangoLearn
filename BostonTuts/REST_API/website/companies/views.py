from django.shortcuts import get_object_or_404
from rest_framework.views import *
from rest_framework.response import *
from rest_framework import *
from .models import Stock
from .serializers import *

#List all stocks or create a new one
#stocks/<ticker>/
class StockList(APIView):

	def get(self,request):
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many=True)
		return Response(serializer.data)

	def post(self):
		pass
