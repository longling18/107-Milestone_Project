from django.contrib.auth.backends import ModelBackend

class CustomBackend(ModelBackend):
    def user_can_authenticate(self, user):
        return not user.is_superuser