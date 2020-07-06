import random
import json
import time
from textblob import TextBlob
from adv_input import *


def topic_conversation(name, s_r, p_info,  mood):
    import copy
    questions = s_r["topic_questions"]
    topics = copy.deepcopy(s_r["topics"])
    rounds = random.randint(3,4)
    for i in range(0, random.randint(3, 4)):
        # chose how to ask a question
        question = random.choice(questions)
        questions.remove(question)
        # chose a topic
        topic = random.choice(list(topics))
        # computer view in the topic
        comp_opinion = topics[topic]
        del topics[topic]

        ans = smart_input(question + topic + '? ')
        time.sleep(2)
        blob = TextBlob(ans)
        p_info[name][topic] = blob.polarity
        with open('people.json', 'r') as fp:
            json.dump(p_info, open("people.json", 'w'))
        if blob.polarity > 0.5:
            print('OMG you really love ' + topic)
        elif blob.polarity > 0.1:
            print('Well, you clearly like ' + topic)
        elif blob.polarity < -0.5:
            print('Woof, you totally hate ' + topic)
        elif blob.polarity < -0.1:
            print("So you don't like " + topic)
        else:
            print('That is a very neutral view on ' + topic)
        if abs(blob.polarity - comp_opinion) < 0.33:
            print('and I tend to agree with you')
            mood += 2
        elif blob.polarity > comp_opinion:
            print('I disagree ', topic, 'is worse than that')
            mood -= 1
        else:
            print('I disagree ', topic, 'is better than that')
            mood -= 2
        if mood < 4:
            print('OK I have had enough of your silly opinions')
            break
