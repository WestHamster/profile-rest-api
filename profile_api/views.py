from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status   #returning responses from API to be added in POST handler

from profile_api import serializers

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
