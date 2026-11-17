from collections.abc import Callable
from typing import cast
from datetime import datetime


from interfaces.base import Interface
from models.events_handler import EventsHandler
from models.dataclasses.user import User, UserHandler


class NotificationInterface(Interface):
    
    def __init__(
        self,
        events_handler: EventsHandler,
        user_handler: UserHandler
    ) -> None:
        
        super().__init__(["admin", "user"])
        
        self.user_handler: UserHandler = user_handler
        self.events_handler: EventsHandler = events_handler
        self.dispatch_dict: dict[str, Callable[[], None]] = {
            "ver": self.show_notifications,
            "sair": lambda: None
        }
    
    
    def show_notifications(self) -> None:
        if not self.user_handler.is_user_set():
            return
        
        user: User = cast(User, self.user_handler.user)
        events: dict[str, dict[str, str]] | None = self.events_handler.get_events(user.id)
        
        if events is None:
            return
        
        for timestamp, event in events.items():
            dt: datetime = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            print(f"[{dt}]: {event['message']}")
    
    
    def run(self) -> None:
        while True:
            self.show_available_commands()
            entry: str = input(">>> ")
            
            if entry == "sair":
                return
            
            action: Callable[[], None] | None = self.dispatch_dict.get(entry, None)
            
            if action is not None:
                action()
            
            