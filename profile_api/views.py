from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as fuction (get ,post ,patch ,put ,delete)',
            'Is similar to a traditional Django View',
            'Gives most control over application logic',
            'Is mapped to URLs'
        ]     #all features of APIView

        return Response({'message':'Hello','an_apiview': an_apiview})       #converts Response to JSON so it needs to be a list or a dictionary
