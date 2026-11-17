from typing import Any
from datetime import datetime

from services.json_handler import JSONHandler


class EventsHandler:
    def __init__(self, json_handler: JSONHandler) -> None:
        self.json_handler: JSONHandler = json_handler
    
    
    def get_events(self, user_id: str) -> dict[str, dict[str, str]] | None:
        data: dict[str, Any] = self.json_handler.read_json()
        
        return data.get(user_id, None)
    
    
    def new_event(
        self,
        user_id: str,
        event_type: str,
        message: str
    ) -> None:
        
        data: Any = self.json_handler.read_json(default={})
        
        if user_id not in data:
            data[user_id] = {}
        
        data[user_id][datetime.now().strftime("%Y-%m-%d %H:%M:%S")] = {
            "type": event_type,
            "message": message
        }
        
        self.json_handler.write_json(data)