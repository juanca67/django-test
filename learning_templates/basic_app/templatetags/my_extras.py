from django import template

register = template.Library()

@register.filter(name='cutting')
def cutting(value, arg):
    """
    This cut out all values of 'arg' from the string
    """
    return value.replace(arg,'Hola')

# register.filter('cutting', cutting)
