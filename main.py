import json

with open('stock_responses.json', 'r') as fp:
    stock_responses = json.load(fp)
with open('people.json', 'r') as fp:
    person_info = json.load(fp)

from parser import *
from introduction import *
from topics import *
from advising import *
from conclusion import *


mood = random.randint(3, 10)
name = intro(stock_responses, person_info, mood)
topic_conversation(name, stock_responses, person_info, mood)
mood = advice_generator(name, mood, stock_responses, person_info)
conclude(name)
