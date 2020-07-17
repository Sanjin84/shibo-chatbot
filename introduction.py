import json
from textblob import TextBlob
from adv_input import *

print("introduction loading")

with open('stock_responses.json', 'r') as fp:
    stock_responses = json.load(fp)
with open('people.json', 'r') as fp:
    person_info = json.load(fp)


def introduce_human(s_r, p_info, mood):
    name, familiar = identify_user(s_r, p_info, mood)
    if familiar:
        ask_how_are_you(name, s_r, mood, familiar=True)
    if not familiar:
        get_user_info(stock_responses, person_info, name)
        ask_how_are_you(name, s_r, mood, familiar=False)
    return name


def identify_user(s_r, p_info, mood):
    if mood > 5:
        name = smart_input(random.choice(s_r["good_hellos"]))
    else:
        name = smart_input(random.choice(s_r["bad_hellos"]))
    familiar = False
    if name in p_info:
        familiar = True
    return name, familiar


def get_user_info(s_r, p_info, name):
    p_info[name] = {"age": 0, "city": 0, "nickname": 0}
    ans = smart_input('Do you have nickname? ')
    if 'yes' in ans.lower() or 'y' in ans.lower():
        nickname = smart_input('what is your nickname: ')
        print('Good to meet you ' + nickname)
    else:
        nickname = name + name[-1] + 'y'
        print('I will call you ' + nickname)
    p_info[name]['nickname'] = nickname
    p_info[name]['age'] = int(input('How old are you? '))
    p_info[name]['city'] = smart_input('which city do you live in? ')
    with open('people.json', 'r') as fp:
        json.dump(p_info, open("people.json", 'w'))


def ask_how_are_you(name, s_r, mood, familiar):
    if familiar:
        response = random.choice(s_r["familiar_greetings"])
    if not familiar:
        response = random.choice(s_r["unfamiliar_greetings"])
    ans = smart_input(response.replace('NAME', name))
    blob = TextBlob(ans)
    if blob.polarity > 0.1 and mood >= 5:
        print('Glad you are doing well')
    elif blob.polarity > 0.1 and mood <= 5:
        print('Yea yea yea whatever ')
    elif blob.polarity < -0.1:
        print('I feel your pain human')
    else:
        print('Seems like you are OK')
