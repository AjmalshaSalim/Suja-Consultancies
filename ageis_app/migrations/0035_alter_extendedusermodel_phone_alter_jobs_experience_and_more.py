# Generated by Django 4.2.7 on 2024-05-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ageis_app", "0034_merge_20240408_1412"),
    ]

    operations = [
        migrations.AlterField(
            model_name="extendedusermodel",
            name="phone",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="experience",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="salary",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="website_link",
            field=models.CharField(max_length=100),
        ),
    ]
