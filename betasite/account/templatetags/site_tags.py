from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import markdown



register = template.Library()


@register.filter(name='indented')
def indent_text(text, classes=''):
    classes = 'indented ' + classes
    text = text.replace('\t', f'<p class="{classes}">')
    text = text.replace('\n', '</p>')
    if not text.endswith("</p>"):
        text += '</p>'

    return format_html(text)



@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
