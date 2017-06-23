from django import template


register = template.Library()


@register.inclusion_tag('form/default_field.html')
def default_field(field):
    css_classes = []
    field_type = field.field.widget.__class__.__name__.lower()

    if field_type == 'textarea':
        css_classes.append('textarea')
    elif field_type == 'textinput':
        css_classes.append('input')

    if field.errors:
        css_classes.append('is-danger')

    field.field.widget.attrs['placeholder'] = field.label
    field.field.widget.attrs['class'] = ' '.join(css_classes)

    return {
        'field': field,
    }


@register.filter
def field_type(field):
    return field.field.widget.__class__.__name__.lower()
