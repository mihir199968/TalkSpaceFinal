from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import openai
import requests

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_out_of_domain"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(text="Out of domain !")
        previous_response = tracker.latest_message.get('text')
        # dispatcher.utter_message("Your previous response was: {}".format(previous_response))
        # # dispatcher.utter_message(self.search_and_get_response(previous_response))
        # # openai.api_key = "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"
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Authorization': 'Bearer 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'
        # }
        #
        # data = {
        #     "model": "gpt-3.5-turbo",
        #     'messages': "virat",
        #     'temperature': 0.5,
        #     'max_tokens': 50,
        #     'stop': '\n'
        # }
        openai.api_key = "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"

        prompt = previous_response
        model = "text-davinci-002"
        temperature = 0.7
        max_tokens = 100

        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        dispatcher.utter_message(response.choices[0].text)
        print(response.choices[0].text)
        #
        # # Send the API request and extract the response
        # response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

        # if response.status_code == 200:
        #     output_text = response.json()['choices'][0]['text']
        # else:
        #     output_text = "Sorry, I couldn't understand that."

        # Send the generated response to the user
        # dispatcher.utter_message(text=output_text)

        return []
