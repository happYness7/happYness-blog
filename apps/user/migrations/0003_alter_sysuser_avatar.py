# Generated by Django 5.1.3 on 2025-04-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_rename_avater_sysuser_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sysuser",
            name="avatar",
            field=models.CharField(
                default="default.jpg", max_length=255, null=True, verbose_name="头像"
            ),
        ),
    ]
