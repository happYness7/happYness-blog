# Generated by Django 5.1.3 on 2025-06-09 00:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_alter_comment_from_user"),
        ("user", "0004_alter_sysuser_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="for_id",
            field=models.IntegerField(null=True, verbose_name="关联对象ID"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="to_user",
            field=models.ForeignKey(
                default="游客",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_comments",
                to="user.sysuser",
                verbose_name="被回复人",
            ),
        ),
    ]
