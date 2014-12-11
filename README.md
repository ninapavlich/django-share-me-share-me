django-social-share-settings
=======================

Model and front end library for choosing and integrating social media share widgets, similar to AddThis.


#Usage:


```python
#settings.py


	INSTALLED_APPS = (
    ...
    'django_social_share_settings',
    ...
    )
```

```
> python manage.py schemamigration django_social_share_settings --initial
> python manage.py migrate django_social_share_settings
```