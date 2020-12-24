from django.apps import AppConfig

# apps.py是子应用的配置,整个配置只对子应用起作用
class BookConfig(AppConfig):
    name = 'book'
