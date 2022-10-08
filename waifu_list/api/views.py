import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from .models import Waifu
from .serializers import WaifuSerializer


class WaifuApiView(APIView):
    # Add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        payload = json.loads(request.body)
        name = payload.get("name")

        # waifus = Waifu.objects.filter(name = payload["name"])
        # serializer = WaifuSerializer(waifus, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'Success!'}, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)
        missingFields = []
        if "name" not in payload:
            missingFields.append("name")
        if "anime" not in payload:
            missingFields.append("anime")
        if "rank" not in payload:
            missingFields.append("rank")
        if "description" not in payload:
            missingFields.append("description")
        if "image" not in payload:
            missingFields.append("image")
        else:
            name = payload.get("name")
            anime = payload.get("anime")
            rank = payload.get("rank")
            description = payload.get("description")
            image = payload.get("image")
        
        if len(missingFields) > 0:
            return Response({'message': 'Missing fields: ' + str(missingFields)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            waifu = Waifu(name=name, anime=anime, rank=rank, description=description, image=image)
            waifu.save()
            serializer = WaifuSerializer(waifu)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class WaifuApiGetAll(generics.ListAPIView):
    queryset = Waifu.objects.all()
    serializer_class = WaifuSerializer
