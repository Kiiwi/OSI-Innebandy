
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "0cb8b7f7-babc-432a-a747-2094ee17b8e807d5a3b6-5217-4a82-a036-7146213d488edb34c1ea-dd46-4bec-982e-f1ddb0f9aa01"
NEVERCACHE_KEY = "74ffdeab-af94-4c3e-ae78-c637e57ac9463b7d177a-c03a-4fd9-a6ed-755946a8e658d19d1dd3-5ad1-4a7b-8414-0bd22dcc9873"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
