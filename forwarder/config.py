from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5250709185:AAG8bcU7n9OEBDeD6thKv_gRcAvw-XJijVI"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001728410290]# List of chat id's to forward messages from.
    TO_CHATS = [-1001469717002]# List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 16
   
    
