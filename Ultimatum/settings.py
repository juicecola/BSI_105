from os import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# List of oTree apps you want to include in your project.
INSTALLED_APPS = ['otree', 'mini_ultimatum']  # Add 'mini_ultimatum' to the installed apps list

# Use the following for the app directory setting
# The path to your project's templates directory
APP_DIRS = [BASE_DIR / "templates"]

SESSION_CONFIGS = [
    dict(
        name='mini_ultimatum',
        display_name="Mini Ultimatum Game",
        app_sequence=['mini_ultimatum'],
        num_demo_participants=3,
    ),
]

# If you have other session configurations, you can add them to SESSION_CONFIGS.

# Set your project-specific configurations in SESSION_CONFIG_DEFAULTS if needed.
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'

# Define whether to use points in your project.
USE_POINTS = True

# Define the rooms for your project if needed.
ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(
        name='live_demo',
        display_name='Room for live demo (no participant labels)',
    ),
]

ADMIN_USERNAME = 'admin'
# For security, it's best to set the admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# Optionally, you can add content to the demo page intro HTML.
DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

SECRET_KEY = '1471865566541'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': APP_DIRS,  # Use the APP_DIRS setting
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

