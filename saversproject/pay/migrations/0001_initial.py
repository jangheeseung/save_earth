# Generated by Django 2.2.1 on 2019-08-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg', models.CharField(max_length=45)),
                ('pay_method', models.CharField(max_length=45)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('buyer_email', models.CharField(blank=True, max_length=45, null=True)),
                ('buyer_name', models.CharField(blank=True, max_length=45, null=True)),
                ('buyer_tel', models.CharField(blank=True, max_length=45, null=True)),
                ('buyer_addr', models.CharField(blank=True, max_length=45, null=True)),
                ('buyer_postcode', models.CharField(blank=True, max_length=45, null=True)),
                ('m_redirect_url', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
