from functools import lru_cache
from app.settings.config import get_settings
import requests

@lru_cache()
def get_session_manager():
    return SessionManager()

class SessionManager:
    def __init__(self):
        self.session = requests.Session()
        self.set_proxy()

    def set_proxy(self):
        settings = get_settings()
        if settings.http_proxy != "" and settings.https_proxy != "":
            self.session.proxies = {
                "http": settings.http_proxy,
                "https": settings.https_proxy,
            }
            print( f"Proxy ON!!" )
        else:
            print( f"Proxy OFF!!" )
    
    def get_session(self):
        return self.session
    
    def close_session(self):
        self.session.close()