# Generated by Django 5.0.8 on 2024-08-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Bid", "0004_rename_mage_creationdata_image_creationdata_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creationdata",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
