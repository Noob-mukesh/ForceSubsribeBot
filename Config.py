import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 16574790))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', "c408c6b40e1ebd04b76c7d04a8de1dad")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "5658314356:AAEIWcIyXBsQhRrltN_Nki6Ra5GcrTY522s")
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    OWNER_ID=5935608297
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', )
    if MUST_JOIN.startswith("@"):
        
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = ""
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    OWNER_ID=5935608297
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

DEVS = [5935608297]
