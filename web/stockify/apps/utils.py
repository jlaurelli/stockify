import bleach
import json as jsonlib

@register.filter
def json(value):
    """Safe jsonify filter."""
    uncleaned = jsonlib.dumps(value)
    clean = bleach.clean(uncleaned)
    return mark_safe(clean)
