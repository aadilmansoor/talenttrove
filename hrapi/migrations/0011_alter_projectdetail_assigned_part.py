# Generated by Django 4.2.5 on 2024-05-22 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapi', '0010_rename_title_meeting_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='assigned_part',
            field=models.CharField(max_length=100),
        ),
    ]
