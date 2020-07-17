import random
import json
import copy
from textblob import TextBlob
from adv_input import *


def talk_about_topics(name, s_r, p_info, mood):
    questions = s_r["topic_questions"]
    topics = copy.deepcopy(s_r["topics"])
    rounds = random.randint(3, 4)
    for i in range(0, rounds):
        # chose how to ask a question
        question = random.choice(questions)
        questions.remove(question)
        # chose a topic
        topic = random.choice(list(topics))
        # computer view in the topic
        comp_opinion = topics[topic]
        del topics[topic]

        ans = smart_input(question + topic + '? ')
        user_opinion = get_user_opinion(topic, ans, p_info, name)

        if abs(user_opinion - comp_opinion) < 0.33:
            print('and I tend to agree with you')
            mood += 2
        elif user_opinion > comp_opinion:
            print('I disagree ', topic, 'is worse than that')
            mood -= 1
        else:
            print('I disagree ', topic, 'is better than that')
            mood -= 2
        if mood < 4:
            print('OK I have had enough of your silly opinions')
            return mood
    return mood


def get_user_opinion(topic, topic_description, p_info, name):
    blob = TextBlob(topic_description)
    user_opinion = blob.polarity
    # Write human opinion to people.json
    p_info[name][topic] = user_opinion
    with open('people.json', 'r') as fp:
        json.dump(p_info, open("people.json", 'w'))
    if user_opinion > 0.5:
        print('OMG you really love ' + topic)
    elif user_opinion > 0.1:
        print('Well, you clearly like ' + topic)
    elif user_opinion < -0.5:
        print('Woof, you totally hate ' + topic)
    elif user_opinion < -0.1:
        print("So you don't like " + topic)
    else:
        print('That is a very neutral view on ' + topic)
    return user_opinion
