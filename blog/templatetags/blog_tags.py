from django import template

register = template.Library()

@register.simple_tag
def mediapath(path):
    if path:
        return f"/media/{path}"
    return f"/media/no_photo.jpg"
