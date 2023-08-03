import marvin
from marvin import ai_fn

marvin.settings.openai.api_key = "YOUR OPENAI KEY"

@ai_fn
def sentiment(text: str) -> float:
    """
    Given `text`, returns a number between 1 (positive) and -1 (negative)
    indicating its sentiment score.
    """


print("Text 1:", sentiment("I love working with Marvin!"))
print("Text 2:", sentiment("These examples could use some work..."))
