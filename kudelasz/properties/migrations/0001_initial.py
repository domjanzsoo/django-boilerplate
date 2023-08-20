# Generated by Django 4.2.2 on 2023-08-12 20:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('offer_type', models.CharField(choices=[('sale', 'Rental'), ('rent', 'For Sale')], max_length=4)),
                ('price', models.PositiveBigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
