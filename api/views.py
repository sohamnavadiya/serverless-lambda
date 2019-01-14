from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PingView(APIView):
    def get(self, request):
        return Response({
            "status": "PONG"
        }, status=status.HTTP_200_OK)
