from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalculateRouteSerializer, GenerateMapUrlSerializer
from geopy.distance import geodesic

class CalculateRouteView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CalculateRouteSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            start_position = data['startPosition']
            points = data['points']
            average_speed = data['averageSpeed']

            response_data = {
                "startPosition": start_position,
                "points": points,
                "averageSpeed": average_speed
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenerateMapUrlView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = GenerateMapUrlSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            path = "|".join([f"{point['longitude']},{point['latitude']}" for point in data['path']])
            map_url = f"https://maps.example.com/?path={path}"
            response_data = {"mapUrl": map_url}
            return Response(response_data, status=status.HTTP_200_OK)
        print(serializer.errors)  # Affichage des erreurs de validation
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###f"..." : C'est une f-string (formatted string literal), introduite dans Python 3.6. Elle permet d'incorporer des expressions Python directement dans des chaînes de caractères en utilisant des accolades {}.###