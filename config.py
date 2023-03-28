import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "28809795"))
    API_HASH = os.environ.get("API_HASH", "e45a8c555ac1a56d1aa1a80db599489a")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6230948304:AAGU4YLNxKGk5D7DC2GjH4lsoNqr6DB-hf0")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5140363414")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://ruby9ca:ruby@N123@ruby-cluster0.jujt8fe.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "ruby-Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'my')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001986323674"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
