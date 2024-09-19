from django.db import migrations, connection
from pgvector.django import VectorExtension


def create_extension_and_register_vector(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        cursor.execute("SELECT register_vector();")


class Migration(migrations.Migration):

    dependencies = [
        # Add your app's previous migration here
    ]

    operations = [
        migrations.RunSQL(create_extension_and_register_vector),
        VectorExtension(),
    ]
