# Generated by Django 3.2.18 on 2023-04-28 17:06

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),  # noqa
                ('excerpt', models.TextField(blank=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),  # noqa
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vehicle_posts', to=settings.AUTH_USER_MODEL)),  # noqa
                ('likes', models.ManyToManyField(blank=True, related_name='blogpost_like', to=settings.AUTH_USER_MODEL)),  # noqa
            ],
             options={
                'ordering': ['-created_on'],
            },
        ),
    ]
