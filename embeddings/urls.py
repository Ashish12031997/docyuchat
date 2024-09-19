from django.urls import path, include

from embeddings.controllers import healthCheck
from embeddings.controllers.embeddings import FileUploadView
from embeddings.controllers.ask import ask

urlpatterns = [
    path("", healthCheck.health_check, name="health_check"),
    path("upload", FileUploadView.as_view(), name="get_embeddings"),
    path("ask", ask.as_view(), name="ask"),
]
