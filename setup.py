from distutils.core import setup

setup(
    name='django-gravatar',
    version='0.1.0',
    description='Basic Gravatar support with helper methods and templatetags.',
    author='Tristan Waddington',
    author_email='tristan.waddington@gmail.com',
    url='https://github.com/twaddington/django-gravatar',
    packages=['django_gravatar', 'django_gravatar.templatetags'],
    classifiers=[
        'Development Status :: 3 - Alpha', # 4 Beta, 5 Production/Stable
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
