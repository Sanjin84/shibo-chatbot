import time
import random
import nltk

nltk.download('nps_chat')
posts = nltk.corpus.nps_chat.xml_posts()[:10000]


def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features


featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))


def smart_input(st):
    text = input(st)
    if text == '':
        print('That is not an answer, try again:')
        text = input(st)

    while 'Question' in classifier.classify(dialogue_act_features(text)):
        print("I dont answer questions")
        print("so lets try this again")
        text = input(st)
        delay = random.uniform(1, 3)
        time.sleep(delay)
    delay = random.uniform(1, 3)
    time.sleep(delay)
    return text


ans = smart_input('Who are you')
print(ans)
'''
line = 'when are you going to come to bed honey'
print(type(classifier.classify(dialogue_act_features(line))))
'''
