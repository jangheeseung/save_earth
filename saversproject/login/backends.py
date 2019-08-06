from django.contrib.auth import get_user_model
import logging

UserModel = get_user_model()

class MyAuthBackend(object):
    def authenticate(self, email, password):
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            else:
                return None
        except user.DoesNotExist:
            logging.getLogger("error_logger").error("user with login %s does not exists " % login)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except user.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None

    def user_can_authenticate(self, user):
        is_active = getattr(user,'is_active', None)
        return is_active or is_active is None
