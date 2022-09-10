# Generated by Django 4.1.1 on 2022-09-10 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65, verbose_name='작품 제목')),
                ('price', models.IntegerField(verbose_name='작품 가격')),
                ('size', models.IntegerField(verbose_name='작품 호수')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'arts',
            },
        ),
        migrations.CreateModel(
            name='Exbihition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65, verbose_name='전시 이름')),
                ('start', models.DateField(verbose_name='전시 시작일')),
                ('end', models.DateField(verbose_name='전시 종료일')),
                ('arts', models.ManyToManyField(to='gallery.art')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'exbihitions',
            },
        ),
    ]