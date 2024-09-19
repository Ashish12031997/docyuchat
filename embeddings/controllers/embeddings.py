import ast
import json
import math
import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from embeddings.serializers.file_upload_serializer import UploadSerializer
from embeddings.controllers.token_counter import get_total_embeddings_cost
from embeddings.controllers.openai import OpenAI
from embeddings.models import Resume


class FileUploadView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            # Access the file in memory
            uploaded_file = serializer.validated_data["file_uploaded"]
            content = uploaded_file.read().decode("utf-8")
            total_cost = get_total_embeddings_cost(content)
            print("total cost", content)
            embedded_text = OpenAI().get_embedding(content)
            resume = Resume(
                name=uploaded_file.name,
                vector=embedded_text,
                summary=content,  # Assuming you want to store the file content as summary
            )
            resume.save()
            return Response({"message": "File received"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
