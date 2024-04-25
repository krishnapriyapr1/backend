from rest_framework import generics
from rest_framework.views import APIView
from events.models import Event
from rest_framework import viewsets
from events.serializers import EventSerializer,UserSerializer
from rest_framework.response import Response

class SignUpView(APIView):

    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class EventListCreate(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


