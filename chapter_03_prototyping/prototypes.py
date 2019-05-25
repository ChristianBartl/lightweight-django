import sys

from django.conf import settings


settings.configure(
    DEBUG=True,
    SECRET_KEY='^=2!_ma7p+#^=top$!84d5r77m#708u#kso90j$l42u-vze%rf',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
      'django.contrib.staticfiles',
      'sitebuilder',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        },
    ),
    STATIC_URL='/static/',
)


if '__name__' == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)