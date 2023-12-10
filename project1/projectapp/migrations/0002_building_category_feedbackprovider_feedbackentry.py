# Generated by Django 4.2.5 on 2023-12-10 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
                ('building_name', models.TextField()),
            ],
            options={
                'db_table': 'building',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.TextField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.building')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='FeedbackProvider',
            fields=[
                ('provider_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('college', models.CharField(max_length=255)),
                ('is_anonymous', models.BooleanField()),
            ],
            options={
                'db_table': 'feedback_provider',
            },
        ),
        migrations.CreateModel(
            name='FeedbackEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedback_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.building')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.category')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.feedbackprovider')),
            ],
            options={
                'db_table': 'feedback_entry',
            },
        ),
    ]
