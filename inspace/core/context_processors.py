from django.conf import settings


def common(request):
    return {
        'INSPACE_LOGO_URL': settings.INSPACE_LOGO_URL,
    }
