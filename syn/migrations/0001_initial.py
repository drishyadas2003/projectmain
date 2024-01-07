# Generated by Django 4.2.6 on 2024-01-04 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('about_course', models.CharField(max_length=1000)),
                ('course_overview', models.CharField(max_length=500)),
                ('course_topic', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry_name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Success',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=500)),
                ('a_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syn.course')),
            ],
        ),
        migrations.CreateModel(
            name='Carrerapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='document/')),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syn.course')),
            ],
        ),
    ]
