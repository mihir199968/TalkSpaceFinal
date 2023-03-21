#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## confused path 1
* mood_confused: I m feeling befuddled
  - utter_confused_1

## confused path 2
* mood_confused: I m feeling puzzled
  - utter_confused_1

## confused path 3
* mood_confused: I m feeling baffled
  - utter_confused_1

## frustated path 1
* mood_frustated: I m feeling frustated
  - utter_frustated_1

## frustated path 2
* mood_frustated: I m feeling exasperated
  - utter_frustated_1

## lonely path 1
* mood_lonely: I m feeling lonely
  - utter_lonely_1

## lonely path 2
* mood_lonely: I m feeling alone
  - utter_lonely_1

## lonely path 3
* mood_lonely: I m feeling isolated
  - utter_lonely_1
  
## out of domain 
* fallback: who is virat kolhi?
  - action_out_of_domain


[//]: # (## happy path 1)

[//]: # (* greet: hello there!)

[//]: # (  - utter_greet)

[//]: # (* mood_great: amazing)

[//]: # (  - utter_happy)

[//]: # ()
[//]: # (## happy path 2)

[//]: # (* greet: hello there!)

[//]: # (  - utter_greet)

[//]: # (* mood_great: amazing)

[//]: # (  - utter_happy)

[//]: # (* goodbye: bye-bye!)

[//]: # (  - utter_goodbye)

[//]: # ()
[//]: # (## sad path 1)

[//]: # (* greet: hello)

[//]: # (  - utter_greet)

[//]: # (* mood_unhappy: not good)

[//]: # (  - utter_cheer_up)

[//]: # (  - utter_did_that_help)

[//]: # (* affirm: yes)

[//]: # (  - utter_happy)

[//]: # ()
[//]: # (## sad path 2)

[//]: # (* greet: hello)

[//]: # (  - utter_greet)

[//]: # (* mood_unhappy: not good)

[//]: # (  - utter_cheer_up)

[//]: # (  - utter_did_that_help)

[//]: # (* deny: not really)

[//]: # (  - utter_goodbye)

[//]: # ()
[//]: # (## sad path 3)

[//]: # (* greet: hi)

[//]: # (  - utter_greet)

[//]: # (* mood_unhappy: very terrible)

[//]: # (  - utter_cheer_up)

[//]: # (  - utter_did_that_help)

[//]: # (* deny: no)

[//]: # (  - utter_goodbye)

[//]: # ()
[//]: # (## say goodbye)

[//]: # (* goodbye: bye-bye!)

[//]: # (  - utter_goodbye)

[//]: # ()
[//]: # (## bot challenge)

[//]: # (* bot_challenge: are you a bot?)

[//]: # (  - utter_iamabot)
