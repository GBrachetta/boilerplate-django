import os

import dj_database_url

# Import below from the common config as needed, and append to the list (+=)
from boilerplate.settings.common import INSTALLED_APPS

DEBUG = False

ALLOWED_HOSTS = [os.environ.get("DOMAIN_NAME")]  # Add env variable in Heroku

INSTALLED_APPS += [
    # Add here your new apps for prod only
    "storages",
]

DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}  # Add variable in Heroku

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = "your_smtp_server"  # For ex. 'smtp.google.com'
EMAIL_HOST_USER = os.environ.get(
    "EMAIL_HOST_USER"
)  # Add env variable in Heroku
EMAIL_HOST_PASSWORD = os.environ.get(
    "EMAIL_HOST_PASSWORD"
)  # Add env variable in Heroku
DEFAULT_FROM_EMAIL = os.environ.get(
    "EMAIL_HOST_USER"
)  # Add env variable in Heroku

if "USE_AWS" in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    AWS_STORAGE_BUCKET_NAME = "your-aws-bucket-name"
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    AWS_S3_REGION_NAME = "eu-central-1"
    AWS_ACCESS_KEY_ID = os.environ.get(
        "AWS_ACCESS_KEY_ID"
    )  # nopep8  # Add env variable in Heroku
    AWS_SECRET_ACCESS_KEY = os.environ.get(
        "AWS_SECRET_ACCESS_KEY"
    )  # Add env variable in Heroku
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATICFILES_LOCATION = "static"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    MEDIAFILES_LOCATION = "media"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"
