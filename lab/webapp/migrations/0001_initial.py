# Generated by Django 2.1 on 2018-12-20 14:21

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
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи системы')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название блюда')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('price', models.DecimalField(decimal_places=2, max_digits='8', verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('contact_name', models.CharField(max_length=50, verbose_name='Имя клиента')),
                ('delivery_address', models.CharField(max_length=200, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='OrderFoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='webapp.Food', verbose_name='Блюдо')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='foods', to='webapp.Order', verbose_name='Заказ')),
            ],
        ),
    ]
