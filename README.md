django-social-share-settings
=======================

Model and front end library for choosing and integrating social media share widgets, similar to AddThis.


#CMS Usage:

To make social settings administerable, include django_social_share_settings and rake the database
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

#Template Usage:
To output share icons based on the settings from the cms, use the 
"social_share_settings_tags" template tags. In this case I'm using 
"Font Awesome" to render the icons.
```
#social-share-partial.html
{% load social_share_settings_tags %}

{% get_social_share_links as social_links %}

{% if social_links|length > 0 %}
<ul class="social sticky">
	{% for link in social_links %}
		{% get_social_share_link link object.get_absolute_url object.title as link_url %}
		<li>
			<a href="{{ link_url }}" target="_blank">
				<i class="fa fa-{{link.font_awesome_class}}"></i>
			</a>
		</li>
	{% endfor %}	
</ul>
{% endif %}
```


#Sticky Usage
For sticky behavior, include or compile in the styles and javscript.

See screencast of sticky widget in action: http://screencast.com/t/Gm8Sah4IMQ
```html
#base-template.html
<!-- Include Font Awesome  for easier social icons -->
<link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet" />

<!-- Include js plugin and css or compile into your source js -->
<link rel="stylesheet" href="{% static 'ccl/sticky.min.css' %}"/>
<script src="{% static 'js/sticky.jqueryplugin.js'%}"></script>
<script>
    $(".sticky").sticky({
        topSelector : "#main",
        bottomSelector : "#footer",
        fixedMargin : 160,
        topMargin : 0,
        bottomMargin : 0
    });
</script>
```
*topSelector* is the selector for the item the sticky widget should top-align with.

*bottomSelector* is the selector for the item the sticky widget should not go below.

*topMargin* refers to the top margin the sticky item will have when aligned to the top selector item

![topMargin example](/../master/docs/screenshots/top_margin.png?raw=true "topMargin example")

*fixedMargin* refers to the top margin the sticky item will have when the screen has scrolled past the top selector item

![fixedMargin example](/../master/docs/screenshots/fixed_margin.png?raw=true "fixedMargin example")

*bottomMargin* refers to the bottom margin the sticky item will have when aligned to the bottom selector item

![bottomMargin example](/../master/docs/screenshots/bottom_margin.png?raw=true "bottomMargin example")