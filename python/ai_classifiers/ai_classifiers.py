import marvin
from marvin import ai_classifier
from enum import Enum

marvin.settings.openai.api_key = "YOUR OPENAI KEY"

@ai_classifier
class AppRoute(Enum):
    """Represents distinct routes command bar for a different application"""
    USER_PROFILE = "/user-profile"
    SEARCH = "/search"
    NOTIFICATIONS = "/notifications"
    SETTINGS = "/settings"
    HELP = "/help"
    CHAT = "/chat"
    DOCS = "/docs"
    PROJECTS = "/projects"
    WORKSPACES = "/workspaces"
AppRoute("update my name")
