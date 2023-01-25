from django import template
from review.models import Sidebar

register = template.Library()

@register.simple_tag()
def get_sidebar():
    return Sidebar.objects.all()
