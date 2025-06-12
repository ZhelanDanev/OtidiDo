from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OtidiDo.accounts'

    def ready(self):
        import OtidiDo.accounts.signals
