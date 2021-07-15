import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer # makes the word a root ex. work is the same as worked, working

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

# load training data
lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', "!", '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern) # tokenize splits the sentence into words ex. hey i am john would be hey, i, am, john

        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# print(documents)

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words)) # eliminates duplicates

# print(words)

classes = sorted(set(classes))

pickle.dump(words, open('ml_data/words.pkl', 'wb'))
pickle.dump(classes, open('ml_data/classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patters = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training, dtype='object')

train_x = list(training[:, 0])
train_y = list(training[:, 1])

# build neural network
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer = sgd, metrics=['accuracy'])

hist = model.fit(np.asarray(train_x).astype(np.int), np.asarray(train_y).astype(np.int), epochs=200, batch_size=5, verbose=1)
model.save('ml_data/chatbotmodel.h5', hist)
print("Done")

# https://www.centervention.com/list-of-emotions-135-words-that-express-feelings/
