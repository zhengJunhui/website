# Generated by Django 2.1 on 2019-05-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(db_index=True, unique=True, verbose_name='IP')),
                ('hostname', models.CharField(max_length=128, verbose_name='Hostname')),
                ('port', models.IntegerField(default=22, verbose_name='Port')),
                ('platform', models.CharField(choices=[('Linux', 'Linux'), ('Windows', 'Windows'), ('BSD', 'BSD'), ('Other', 'Other')], default='Linux', max_length=128, verbose_name='系统平台')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('login_user', models.CharField(blank=True, default='root', max_length=32, verbose_name='管理用户')),
                ('vendor', models.CharField(blank=True, max_length=64, null=True, verbose_name='厂商')),
                ('localtion', models.CharField(blank=True, max_length=64, null=True, verbose_name='区域')),
                ('model', models.CharField(blank=True, max_length=54, null=True, verbose_name='Model')),
                ('cpu_model', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU model')),
                ('cpu_cores', models.IntegerField(null=True, verbose_name='CPU cores')),
                ('memory', models.CharField(blank=True, max_length=64, null=True, verbose_name='Memory')),
                ('disk_total', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Disk total')),
                ('asset_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Asset number')),
                ('os', models.CharField(blank=True, max_length=128, null=True, verbose_name='OS')),
                ('os_version', models.CharField(blank=True, max_length=16, null=True, verbose_name='OS version')),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('comment', models.TextField(blank=True, default='', max_length=128, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_code', models.CharField(default='', help_text='项目代码', max_length=16, unique=True)),
                ('platform_name', models.CharField(default='', help_text='项目平台', max_length=64, unique=True, verbose_name='Platform_name')),
            ],
        ),
        migrations.AddField(
            model_name='assets',
            name='project',
            field=models.ForeignKey(help_text='项目平台', on_delete=False, to='assets.Platform', verbose_name='项目平台'),
        ),
    ]