# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialShareLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(null=True, verbose_name=b'order', blank=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Service Type', choices=[(b'email', b'Email'), (b'twitter', b'Twitter'), (b'facebook', b'Facebook'), (b'googleplus', b'Google Plus'), (b'linkedin', b'LinkedIn'), (b'pinterest', b'Pinterest'), (b'digg', b'Digg'), (b'tumblr', b'Tumblr'), (b'reddit', b'Reddit'), (b'stumbleupon', b'StumbleUpon'), (b'delicious', b'Delicious')])),
                ('title_template', models.TextField(help_text=b'Applicable to all types but Facebook and Google Plus. Available contact variables: {{url}}, {{title}}, {{site}}', null=True, verbose_name='Title Template', blank=True)),
                ('description_template', models.TextField(help_text=b'Applicable to type Email and Tumblr. Available contact variables: {{url}}, {{title}}, {{site}}', null=True, verbose_name='Description Template', blank=True)),
                ('to_template', models.TextField(help_text=b'Applicable to type Email. Available contact variables: {{url}}, {{title}}, {{site}}', null=True, verbose_name='To Template', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialShareSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('track_social_share_clicks', models.BooleanField(default=True, verbose_name='Track Social Share Clicks')),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name_plural': 'Social Share Settings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialShareTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=255, null=True, verbose_name='Domain', blank=True)),
                ('path', models.CharField(max_length=255, null=True, verbose_name='Path', blank=True)),
                ('full_url', models.CharField(max_length=255, null=True, verbose_name='Full URL', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Service Type', choices=[(b'email', b'Email'), (b'twitter', b'Twitter'), (b'facebook', b'Facebook'), (b'googleplus', b'Google Plus'), (b'linkedin', b'LinkedIn'), (b'pinterest', b'Pinterest'), (b'digg', b'Digg'), (b'tumblr', b'Tumblr'), (b'reddit', b'Reddit'), (b'stumbleupon', b'StumbleUpon'), (b'delicious', b'Delicious')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='socialsharelink',
            name='parent',
            field=models.ForeignKey(to='share_me_share_me.SocialShareSettings'),
            preserve_default=True,
        ),
    ]
