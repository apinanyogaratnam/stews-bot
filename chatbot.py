import random, json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('ml_data/words.pkl', 'rb'))
classes = pickle.load(open('ml_data/classes.pkl', 'rb'))
model = load_model('ml_data/chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]

    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1

    return np.array(bag, dtype='object')


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.asarray([bow]).astype(np.int))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_lst = []
    for r in results:
        return_lst.append({'intent': classes[r[0]], 'probability': str(r[1])})
    
    return return_lst


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break

    return result


if __name__ == '__main__':
    print("Bot is running!")

    while True:
        message = input("input: ")
        ints = predict_class(message)
        res = get_response(ints, intents)
        print(res)