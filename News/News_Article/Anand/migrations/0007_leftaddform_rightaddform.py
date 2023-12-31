# Generated by Django 4.2.1 on 2023-08-21 18:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Anand', '0006_internationalpostform_img_url_sportpostform_img_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='leftaddform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uleftadd', models.TextField(default='')),
                ('ualeftadd', models.TextField(default='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('img_url', models.ImageField(default='', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='rightaddform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urightadd', models.TextField(default='')),
                ('uarightadd', models.TextField(default='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('img_url', models.ImageField(default='', upload_to='images/')),
            ],
        ),
    ]
