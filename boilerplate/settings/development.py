import os

# Import below from the common config as needed, and append to the list (+=)
from boilerplate.settings.common import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

ALLOWED_HOSTS = [
    os.environ.get("DOMAIN_NAME"),  # Add in .env
    "localhost",
    "127.0.0.1",
]

INSTALLED_APPS += [
    "debug_toolbar",
    "mail_panel",
    # Add here your new apps for dev only
]

MIDDLEWARE.insert(
    0,
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}

EMAIL_BACKEND = "mail_panel.backend.MailToolbarBackend"
DEFAULT_FROM_EMAIL = "admin@mail.com"

DEBUG_TOOLBAR_PANELS = [
    "ddt_request_history.panels.request_history.RequestHistoryPanel",
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "mail_panel.panels.MailToolbarPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

INTERNAL_IPS = ["127.0.0.1", "localhost"]  # For debug-toolbar
