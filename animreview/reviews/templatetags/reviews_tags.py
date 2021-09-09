from django import template
from reviews.models import *

register = template.Library()


@register.simple_tag(name='getgen')
def get_genres():
    return Genre.objects.all()


@register.inclusion_tag('reviews/list_genres.html')
def show_genres():
    genres = Genre.objects.all()
    return {'genres': genres}
