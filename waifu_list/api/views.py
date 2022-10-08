import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from .models import Waifu
from .serializers import WaifuSerializer


def index(request):
    '''
    This is just to give the back end a home page.
    '''
    return render(request, "index.html")


class WaifuApiView(APIView):
    # Add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        Get a single waifu entry from the database.
        '''
        payload = json.loads(request.body)
        
        if not payload:
            return Response({'message': 'No data provided!'}, status=status.HTTP_400_BAD_REQUEST)
        if "name" not in payload and "id" not in payload:
            return Response({'message': 'ID or name must be provided!'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if "id" in payload:
                waifu = Waifu.objects.get(id=payload["id"])
            elif "name" in payload:
                waifu = Waifu.objects.get(name=payload["name"])
        except:
            return Response({'message': 'Waifu not found!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer = WaifuSerializer(waifu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

    def post(self, request, *args, **kwargs):
        '''
        Add a new waifu entry to the database.
        '''
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

        # Ensure no duplicate entries
        try:
            waifu = Waifu.objects.get(name=name, anime=anime)
            return Response({'message': 'Waifu already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        try:
            waifu = Waifu(name=name, anime=anime, rank=rank, description=description, image=image)
            waifu.save()
            serializer = WaifuSerializer(waifu)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, *args, **kwargs):
        '''
        Update an existing waifu entry in the database.
        '''
        payload = json.loads(request.body)
        
        if not payload:
            return Response({'message': 'No data provided!'}, status=status.HTTP_400_BAD_REQUEST)
        if "name" not in payload and "id" not in payload:
            return Response({'message': 'ID or name must be provided!'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if "id" in payload:
                waifu = Waifu.objects.get(id=payload["id"])
            elif "name" in payload:
                waifu = Waifu.objects.get(name=payload["name"])
        except:
            return Response({'message': 'Waifu not found!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # This allows for a partial payload with some fields missing
            serializer = WaifuSerializer(waifu, data=payload, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            # This will catch duplicate rank errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, *args, **kwargs):
        '''
        Delete a single waifu entry from the database.
        '''
        payload = json.loads(request.body)

        if not payload:
            return Response({'message': 'No data provided!'}, status=status.HTTP_400_BAD_REQUEST)
        if "name" not in payload and "id" not in payload:
            return Response({'message': 'ID or name must be provided!'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if "id" in payload:
                waifu = Waifu.objects.get(id=payload["id"])
            elif "name" in payload:
                waifu = Waifu.objects.get(name=payload["name"])
        except:
            return Response({'message': 'Waifu not found!'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            waifu.delete()
            return Response({'message': 'Waifu successfully deleted.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class WaifuApiAll(APIView):
    '''
    This is for operations that affect all waifu entries in the database.
    '''
    # Add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        Get all waifu entries from the database.
        '''
        try:
            waifus = Waifu.objects.all()
            serializer = WaifuSerializer(waifus, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, *args, **kwargs):
        '''
        Delete all waifu entries from the database.
        '''
        try:
            Waifu.objects.all().delete()
            return Response({'message': 'All waifus successfully deleted.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)