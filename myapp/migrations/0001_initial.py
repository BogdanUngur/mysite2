# Generated by Django 2.1.2 on 2018-10-28 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('poster', models.CharField(max_length=1000)),
                ('director', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Movie'),
        ),
    ]
