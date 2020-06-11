from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status   #returning responses from API to be added in POST handler
from rest_framework import viewsets

from profile_api import serializers
from profile_api import models

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as fuction (get ,post ,patch ,put ,delete)',
            'Is similar to a traditional Django View',
            'Gives most control over application logic',
            'Is mapped to URLs'
        ]     #all features of APIView

        return Response({'message':'Hello','an_apiview': an_apiview})       #converts Response to JSON so it needs to be a list or a dictionary

    def post(self,request):
        """Create a message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')    #Similarly you can retrieve anything from serializer this way
            message = f'Hello {name}'

            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST      #bad request made to API
                )

    def put(self, request, pk=None):#pk is for specific URL key
        """Handle updating an object"""     #make a request and request is update with entire object
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):#update only the fields provided in request
        """Handle a partial update on an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """To delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""
        a_viewset = [
            'Actions (list,create,retrieve,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'More functionality',
            ]

        return Response({'message':'Router','viewset':a_viewset})

    def create(self,request):
        """Create a new serializer"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by it's ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http-method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http-method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http-method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):#Just like a normal ViewSet class is linked to serialiser
    """Handling create and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
