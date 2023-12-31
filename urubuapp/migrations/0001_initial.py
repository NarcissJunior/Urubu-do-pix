# Generated by Django 4.2.5 on 2023-10-02 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WalletModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=30)),
                ('last_updated', models.DateTimeField(verbose_name='last updated')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urubuapp.user')),
            ],
        ),
    ]
