import time
from textblob import TextBlob
from adv_input import *


def generate_advice(name,mood, s_r, p_info):
    if mood < 4:
        print("I was going to give you some life changing advice . . . but clearly you don't deserve it")
    else:
        all_topics = s_r["topics"]
        candidates = {}
        for topic in all_topics:
            if topic in p_info[name]:
                candidates[topic] = p_info[name][topic]
        advice_topic = max(candidates, key=candidates.get)
        print('Let me give you some advice')
        time.sleep(2)
        print('You need more', advice_topic, 'in your life')
        time.sleep(2)
        if advice_topic == 'football':
            print('You should watch some games of Leeds United')
        if advice_topic == 'Python':
            print('I think you should try programming a chatbot')
        if advice_topic == 'Endgame':
            print('I think you should watch that movie once a day :P')
        if advice_topic == 'AFL':
            print('Its still a rubbish sport but if it makes you happy . . .')
        time.sleep(2)
        ans = smart_input('So what do you think about my advice?')
        blob = TextBlob(ans)
        if blob.polarity > 0.1:
            print('Glad you agree with my advice!')
        elif blob.polarity < -0.1:
            print("Yea you clearly don't know whats good for you")
        else:
            print('You aught to be more enthusiastic, that was life changing advice!')
    return mood
