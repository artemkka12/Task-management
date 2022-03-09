# Generated by Django 3.0.7 on 2022-03-09 17:40

import apps.gallery.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0002_auto_20220309_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.FileField(upload_to=apps.gallery.models.upload_to_user_id),
        ),
    ]
