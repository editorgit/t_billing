# Generated by Django 3.0.4 on 2020-03-06 16:57

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyConversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('initial_currency', models.CharField(max_length=3)),
                ('initial_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('exchange_rate', models.DecimalField(decimal_places=5, max_digits=10)),
                ('converted_currency', models.CharField(max_length=3)),
                ('converted_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'conversions',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_changed_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('balance_currency', djmoney.models.fields.CurrencyField(choices=[('EUR', 'Euro'), ('GBP', 'Pound Sterling'), ('RUB', 'Russian Ruble'), ('USD', 'US Dollar')], default='EUR', editable=False, max_length=3)),
                ('balance', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='EUR', max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'wallet',
            },
        ),
        migrations.CreateModel(
            name='MoneyTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('converter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transfer.MoneyConversion')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receivers', to='transfer.Wallet')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='senders', to='transfer.Wallet')),
            ],
            options={
                'db_table': 'transfers',
            },
        ),
    ]