# Generated by Django 4.2.9 on 2024-04-19 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0014_finalorder"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="final",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="seller.finalorder",
            ),
            preserve_default=False,
        ),
    ]
