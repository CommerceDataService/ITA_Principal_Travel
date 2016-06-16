from django import template
from django.template.defaulttags import register

register = template.Library()

@register.simple_tag
def current_url(request, param, value):
    url = request.GET.copy()
    url[param] = value
    return url.urlencode()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
