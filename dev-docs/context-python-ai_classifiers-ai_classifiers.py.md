# Classifiers Tutorial

This code is importing the ai_classifier and enum modules from marvin. It then sets the openai.api_key to the value of the environment variable "YOUR OPENAI KEY". The @ai_classifier decorator is then used to decorate the AppRoute class. This class defines the different routes that the command bar can be used for. The AppRoute("update my name") line creates an instance of the AppRoute class with the route "/update my name".

# Lets run it

Export the API Key value with your OPENAI key and then run the command below:

```
export MARVIN_OPENAI_API_KEY=&lt;your API key&gt;
```
```

python python/ai_classifiers/ai_classifiers.py

```

Have fun playing experimenting!
