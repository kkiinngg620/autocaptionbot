import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6346310708:AAHGxZI4lFhoOz4ehKA1t365JxLkh7PBkJ8")
      API_ID = int(os.environ.get("APP_ID", "27157998"))
      API_HASH = os.environ.get("API_HASH", "45d09c93e37c9b93b6535949c898f906")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "mr_chaudhary620")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", "1452198353")) 
      DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://BOOMERMAN:BOOMERMAN@cluster0.7iadxlk.mongodb.net/?retryWrites=true&w=majority")
