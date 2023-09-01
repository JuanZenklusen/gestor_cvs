from django.apps import AppConfig


class CvsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cvs_app'
    
    def ready(self):
        import cvs_app.signals