# Generated by Django 5.1.1 on 2024-09-04 21:59

import pgvector.django.vector
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embeddings', '0002_alter_resume_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='summarry',
            new_name='summary',
        ),
        migrations.AlterField(
            model_name='resume',
            name='vector',
            field=pgvector.django.vector.VectorField(blank=True, dimensions=1536, help_text='The vector to resume', null=True),
        ),
    ]
