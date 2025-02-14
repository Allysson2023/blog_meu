import string
from random import SystemRandom
from django.utils.text import slugify

def random_letters(k):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k
    ))

def slugify_new(text):
    return slugify(text)+ '-'  + random_letters(10)

#print(slugify_new('bla bla bla bla bla'))