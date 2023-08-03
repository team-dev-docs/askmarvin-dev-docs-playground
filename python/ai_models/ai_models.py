import marvin
from marvin import ai_model
from pydantic import BaseModel, Field

marvin.settings.openai.api_key = "YOUR OPENAI KEY"

@ai_model
class Location(BaseModel):
    city: str
    state: str = Field(..., description="The two-letter state abbreviation")
Location("The Big Apple")
