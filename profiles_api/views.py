from rest_framework.response import Response
from rest_framework.views import APIView


class HelloAPI(APIView):
    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function(get, post, put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
