# Generated by Django 4.2.9 on 2024-04-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0012_alter_orderitem_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="availability",
            field=models.CharField(
                choices=[("In Stock", "In Stock"), ("Out of Stock", "Out of Stock")],
                max_length=225,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="condition",
            field=models.CharField(
                choices=[("New", "New"), ("Old", "Old")], max_length=225, null=True
            ),
        ),
    ]
