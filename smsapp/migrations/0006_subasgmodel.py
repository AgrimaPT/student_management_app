# Generated by Django 4.2.2 on 2023-09-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0005_asgmntmodel2_delete_asgmntmodel1'),
    ]

    operations = [
        migrations.CreateModel(
            name='subasgmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cla', models.CharField(max_length=20)),
                ('sb', models.CharField(max_length=20)),
                ('numb', models.CharField(max_length=20)),
                ('asg', models.ImageField(upload_to='smsapp/static')),
            ],
        ),
    ]
