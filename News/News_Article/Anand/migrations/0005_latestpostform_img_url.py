# Generated by Django 4.2.1 on 2023-08-19 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anand', '0004_internationalpostform_technicalpostform_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestpostform',
            name='img_url',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
