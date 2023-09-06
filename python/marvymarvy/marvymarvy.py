from marvin import ai_model
from pydantic import BaseModel, Field
@ai_model
class Location(BaseModel):
    city: str
    state: str = Field(..., description="The two-letter state abbreviation")
Location("The Big Apple")
