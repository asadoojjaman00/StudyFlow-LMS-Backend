from django.core.cache import cache
import random

# Generate 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Store OTP in Redis (valid 5 minutes)
def set_otp_in_redis(email, otp):
    cache.set(f"otp:{email}", otp, timeout=300)  # 300 seconds = 5 minutes

# Set resend block to prevent spam (valid 1 minute)
def set_resend_block(email):
    cache.set(f"otp_time:{email}", "1", timeout=60)  # 60 seconds = 1 minute

# Check if user can resend OTP
def can_resend(email):
    return cache.get(f"otp_time:{email}") is None
