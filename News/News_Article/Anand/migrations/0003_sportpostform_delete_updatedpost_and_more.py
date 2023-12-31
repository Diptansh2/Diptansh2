# Generated by Django 4.2.1 on 2023-08-17 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Anand', '0002_alter_registerform_ucourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='sportpostform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usportpost', models.TextField(default='')),
                ('uasportpost', models.TextField(default='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='updatedpost',
        ),
        migrations.AlterField(
            model_name='article',
            name='news_type',
            field=models.CharField(choices=[('latest', 'Latest Article'), ('sport', 'Updated Article'), ('international', 'New Article'), ('tech', 'Technical Article')], default='latest', max_length=20),
        ),
    ]
