# Generated by Django 4.0.6 on 2022-08-04 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0006_alter_chat_id_alter_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='icon',
            field=models.FileField(blank=True, upload_to='message_icons/'),
        ),
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, upload_to='image_image'),
        ),
        migrations.AlterField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
