from django import template

register = template.Library()


@register.filter
def adjust_earnings(total_earnings):
    try:
        if total_earnings > 100000:
            return total_earnings - 10000
        elif total_earnings > 10000:
            return total_earnings - 1000
        elif total_earnings > 1000:
            return total_earnings - 100
        else:
            return total_earnings
    except TypeError:
        return total_earnings
