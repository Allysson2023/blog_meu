from django.core.exceptions import ValidationError


def validate_png(image):
    if not image.name.lower().endswith('.jpg'):
        raise ValidationError('imagem precisa ser PNG')
