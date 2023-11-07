from django import template

register = template.Library()

@register.simple_tag
def mediapath(path):
    if path:
        return f"/media/{path}"
    return f"/media/product_images/no_photo.jpg"
