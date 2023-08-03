```python

from marvin import ai_model
from pydantic import BaseModel, Field

marvin.settings.openai.api_key = "YOUR OPENAI KEY"

@ai_model
class Location(BaseModel):
    city: str
    state: str = Field(..., description="The two-letter state abbreviation")
Location("The Big Apple")
```

This code is using the marvin library to create an AI model for a Location class. The model will be able to answer questions about locations, such as their city and state. The api_key variable is used to authenticate the model with the OpenAI API.

## Lets Run it 

### Copy and paste this command and run it
```
python python/ai_models/ai_models.py
```

Now feel free to play around!
