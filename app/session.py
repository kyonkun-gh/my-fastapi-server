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

    def send_request(self, url: str, method: str, data: dict = None):
        if method.upper() == "GET":
            return self.send_request_get(url)
        elif method.upper() == "POST":
            return self.send_request_post(url, data)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
    
    def send_request_get(self, url: str):
        response = self.session.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response

    def send_request_post(self, url: str, data: dict):
        response = self.session.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response