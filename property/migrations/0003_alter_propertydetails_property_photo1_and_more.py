# Generated by Django 4.2.1 on 2023-05-07 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_propertydetails_propert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='property_photo1',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='property_photo2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='property_photo3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='property_photo4',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
    ]
