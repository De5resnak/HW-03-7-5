from django import template


register = template.Library()

BAN_WORDS = ['fuck', 'bastard']


@register.filter()
def censor(value):
    m = value.split(' ')
    output = ''
    for word in m:
        if word.lower() in BAN_WORDS:
            word = word[0]+'*'*(len(word)-1)
        output += word+' '
    return output
