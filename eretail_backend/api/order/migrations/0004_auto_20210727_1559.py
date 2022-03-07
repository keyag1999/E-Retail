# Generated by Django 3.0.8 on 2021-07-27 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210721_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_names',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_products',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='order.Cart'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]