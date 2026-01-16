from rest_framework.views import APIView
from datetime import datetime
from django.db.models import Sum, Count
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.conf import settings
import os

from Events.models import Event
from .models import Decor
from .serializers import EventSerializer, DecorSerializer

from .models import DecorImage
from .serializers import DecorImageSerializer

# Standard CRUD using ModelViewSet (you already have this)
from rest_framework import viewsets

class DecorViewSet(viewsets.ModelViewSet):
    queryset = Decor.objects.all()
    serializer_class = DecorSerializer



@api_view(['GET'])
def decor_summary(request):
        from_date = request.query_params.get('from')
        to_date = request.query_params.get('to')

        if not from_date or not to_date:
            return Response({"error": "Please provide 'from' and 'to' query parameters."},
                        status=status.HTTP_400_BAD_REQUEST)

        try:
            from_date = datetime.strptime(from_date, "%Y-%m-%d")
            to_date = datetime.strptime(to_date, "%Y-%m-%d")
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."},
                        status=status.HTTP_400_BAD_REQUEST)

        # Filter data in date range
        records = Decor.objects.filter(date__range=[from_date, to_date])

        # Helper function to get summary for each type
        def get_summary(item_type):
            data = records.filter(item=item_type)
            total_count = data.count()
            total_amount = data.aggregate(total=Sum('amount'))['total'] or 0
            return {"count": total_count, "amount": total_amount}

        response_data = {
            "DJ": get_summary("DJ"),
            "Cool Fire": get_summary("Cool Fire"),
            "Ice Pots": get_summary("Ice Pots"),
        }

        return Response(response_data, status=status.HTTP_200_OK)   




# NEW: API to fetch events without decor or without decor_amount
class EventsWithoutDecorAmount(APIView):
    def get(self, request):
        events = (
            Event.objects.filter(decor__isnull=True) |
            Event.objects.filter(decor__decor_amount__isnull=True)
        ).distinct()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



class DecorImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('images')  # try to get multiple
        single_file = request.FILES.get('image')  # try to get single

        if not files and not single_file:
            return Response({"error": "No image provided."}, status=status.HTTP_400_BAD_REQUEST)

        created_images = []

        if files:  # multiple images
            for file in files:
                img = DecorImage.objects.create(image=file)
                created_images.append(img)
        elif single_file:  # single image
            img = DecorImage.objects.create(image=single_file)
            created_images.append(img)

        serializer = DecorImageSerializer(created_images, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DecorImageListView(APIView):
    def get(self, request, *args, **kwargs):
        images = DecorImage.objects.all().order_by('-uploaded_at')
        serializer = DecorImageSerializer(images, many=True)
        return Response(serializer.data)




class CreateImageFolderView(APIView):
    def post(self, request):
        folder_name = request.data.get('folder_name')
        if not folder_name:
            return Response({"error": "folder_name is required"}, status=status.HTTP_400_BAD_REQUEST)

        folder_path = os.path.join(settings.MEDIA_ROOT, 'decor_images', folder_name)
        os.makedirs(folder_path, exist_ok=True)

        return Response({
            "message": f"Folder '{folder_name}' created successfully.",
            "path": f"/media/decor_images/{folder_name}/"
        }, status=status.HTTP_201_CREATED)



# class DecorFoldersWithImagesView(APIView):
#     def get(self, request):
#         base_path = os.path.join(settings.MEDIA_ROOT, 'decor_images')
#         if not os.path.exists(base_path):
#             return Response({"message": "No folders found."}, status=status.HTTP_200_OK)

#         folders_data = []

#         for folder_name in os.listdir(base_path):
#             folder_path = os.path.join(base_path, folder_name)
#             if os.path.isdir(folder_path):
#                 images = []
#                 for file_name in os.listdir(folder_path):
#                     if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
#                         image_url = f"/media/decor_images/{folder_name}/{file_name}"
#                         images.append(image_url)

#                 folders_data.append({
#                     "folder_name": folder_name,
#                     "images": images
#                 })

#         return Response(folders_data, status=status.HTTP_200_OK)


class DecorFoldersWithImagesView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        base_path = os.path.join(settings.MEDIA_ROOT, 'decor_images')
        if not os.path.exists(base_path):
            return Response({"message": "No folders found."}, status=status.HTTP_200_OK)

        folder_name = request.query_params.get('name', None)

        # ✅ If specific folder requested
        if folder_name:
            folder_path = os.path.join(base_path, folder_name)
            if not os.path.isdir(folder_path):
                return Response({"error": "Folder not found."}, status=status.HTTP_404_NOT_FOUND)

            images = []
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    image_url = f"/media/decor_images/{folder_name}/{file_name}"
                    images.append(image_url)

            return Response({
                "folder_name": folder_name,
                "images": images
            }, status=status.HTTP_200_OK)

        # ✅ Else list all folders
        folders_data = []
        for folder in os.listdir(base_path):
            folder_path = os.path.join(base_path, folder)
            if os.path.isdir(folder_path):
                images = []
                for file_name in os.listdir(folder_path):
                    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                        image_url = f"/media/decor_images/{folder}/{file_name}"
                        images.append(image_url)

                folders_data.append({
                    "folder_name": folder,
                    "images": images
                })

        return Response(folders_data, status=status.HTTP_200_OK)