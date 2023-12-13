# utils.py

import pyotp
from .models import CustomUser
from django_otp.plugins.otp_totp.models import TOTPDevice

def get_user_otp_secret(user):
    try:
        totp_device = TOTPDevice.objects.filter(user=user, confirmed=True).order_by('-confirmed_at').first()
        return totp_device.key if totp_device else None
    except CustomUser.DoesNotExist:
        return None

def validate_otp(user, otp_token):
    user_otp_secret = get_user_otp_secret(user)

    if user_otp_secret is None:
        return False

    totp = pyotp.TOTP(user_otp_secret)
    return totp.verify(otp_token)
