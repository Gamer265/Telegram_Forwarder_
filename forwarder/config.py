from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5076883469:AAGCLYTEaE_4mcJZhbP5ja3FNqqmwU_NMKI"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001102718567,-1001129438703,-1001189750195]# List of chat id's to forward messages from.
    TO_CHATS = [-1001439901698]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
