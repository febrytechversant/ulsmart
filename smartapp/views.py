from django.shortcuts import render
from smartapp.serializers import SiteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.sites.models import Site

#@api_view([..])
#@permission_classes((permissions.AllowAny,))
class SitesList(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        print serializer.data,'ddddddddddddddd'
        return Response(serializer.data)

