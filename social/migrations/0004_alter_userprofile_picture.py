# Generated by Django 3.2 on 2021-04-29 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/default.png', upload_to='uploads/profile_pictures'),
        ),
    ]