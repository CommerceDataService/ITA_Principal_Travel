from django import template

register = template.Library()

@register.simple_tag
def current_url(request, param, value):
    url = request.GET.copy()
    url[param] = value
    return url.urlencode()
