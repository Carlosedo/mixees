import simplejson

from django import template
from django.core import serializers
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def jsonify(value):
    return mark_safe(simplejson.dumps(value))

@register.filter
def jsonify_object(value):
    return mark_safe(serializers.serialize("json", value))
