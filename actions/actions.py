
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionTriggerSearch(Action):
    """
    Action to trigger Enterprise Search 
    for knowledge-based questions.
    """
    
    def name(self) -> Text:
        return "action_trigger_search"

    def run(self, dispatcher, tracker, domain):
        """
        Simple search action with canary test.
        """
        
        user_message = tracker.latest_message.get("text", "")
        
        # Canary test
        if "canary" in user_message.lower():
            response = "The safe color for deployments is ultramarine kiwi."
        else:
            # Let Rasa Pro handle the search automatically
            response = f"Searching for: '{user_message}'"
        
        dispatcher.utter_message(text=response)
        return []

