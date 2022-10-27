from django import template

register = template.Library()

# 장고에서 빼기를 이용하기 위한 함수


@register.filter
def sub(value, arg):
    return value - arg
