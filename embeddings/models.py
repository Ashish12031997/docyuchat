from django.db import models
from pgvector.django import VectorField, IvfflatIndex, HnswIndex


class Resume(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    vector = VectorField(
        dimensions=1536, help_text="The vector to resume", null=True, blank=True
    )
    updated_ts = models.DateTimeField(auto_now_add=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    summary = models.CharField()

    class Meta:
        db_table = "resume"
        indexes = [
            HnswIndex(
                fields=["vector"],
                name="resume_vector_index",
                m=16,
                ef_construction=64,
                opclasses=["vector_cosine_ops"],
            )
        ]
