from django.db import models
from pgvector.django import VectorField, IvfflatIndex


class Resume(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    vector = VectorField(
        dimension=768, help_text="The vector to resume", null=True, blank=True
    )
    updated_ts = models.DateTimeField(auto_now_add=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    summarry = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "public.resume"
        indexes = [
            IvfflatIndex(
                fields=["vector"],
                name="resume_vector_index",
                similarity=0.7,  # High similarity for cosine similarity
                params={"num_threads": 4},  # Use 4 threads for indexing
            )
        ]
