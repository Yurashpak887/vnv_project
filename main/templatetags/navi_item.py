from django import template
from main.models import Menu

register = template.Library()

@register.inclusion_tag('nav.html', takes_context=True)
def all_navi(context):
    navi_items = Menu.objects.all()
    current_item = context['request'].path  # Отримуємо URL поточної сторінки
    print(current_item)
    return {'navi_items': navi_items, 'current_item': current_item}
