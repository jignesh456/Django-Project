# Generated by Django 3.1.7 on 2021-06-11 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_nm', models.CharField(default='', max_length=200)),
                ('cust_em', models.EmailField(default='', max_length=200)),
                ('cust_con', models.CharField(default='', max_length=50)),
                ('cust_add1', models.TextField(default='')),
                ('cust_add2', models.TextField(default='')),
                ('cust_regi_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cust_profile', models.ImageField(blank=True, default='', max_length=300, null=True, upload_to='Cust_Pic/')),
                ('comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_details')),
            ],
        ),
    ]
