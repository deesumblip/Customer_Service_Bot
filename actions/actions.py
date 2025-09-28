
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionCheckCanary(Action):
    """
    Custom action to check for canary test before triggering search.
    """
    
    def name(self) -> Text:
        return "action_check_canary"

    def run(self, dispatcher, tracker, domain):
        """
        Check for canary test first.
        """
        
        user_message = tracker.latest_message.get("text", "")
        
        # Canary test
        if "canary" in user_message.lower():
            dispatcher.utter_message(text="The safe color for deployments is ultramarine kiwi.")
            dispatcher.utter_message(text="What else can I help you with?")
            return [SlotSet("canary_detected", True)]
        
        return []

