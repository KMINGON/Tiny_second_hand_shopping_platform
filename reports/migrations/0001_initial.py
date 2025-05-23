# Generated by Django 5.2 on 2025-04-24 17:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0003_chatreport'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(blank=True)),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_chatreport', to='chat.chat')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_chatreport', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('reporter', 'message')},
            },
        ),
        migrations.CreateModel(
            name='ProductReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(blank=True)),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('reported_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='products.product')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_productreport', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('reporter', 'reported_product')},
            },
        ),
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('reported_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('reporter', 'reported_user')},
            },
        ),
    ]
