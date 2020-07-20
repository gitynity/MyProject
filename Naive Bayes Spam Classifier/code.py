import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

 
data_json_file = 'spam.csv'
data = pd.read_csv(data_json_file , engine = "python")
print(data.tail())

 
print(data.shape)

 
vectorizer = CountVectorizer(stop_words='english')

 
all_features=vectorizer.fit_transform(data.v2)

 
x_train , x_test , y_train , y_test = train_test_split(all_features,data.v1, test_size=0.3 , random_state=88)

 
print(x_train.shape)

 
print(x_test.shape)

 
classifier = MultinomialNB()

 
classifier.fit(x_train,y_train)

 
correctly_classified=(y_test==classifier.predict(x_test)).sum()

 
print(f'Correctly classified mails are {correctly_classified}')

 
incorrectly_classified=(y_test!=classifier.predict(x_test)).sum()

 
print(f'Incorrectly classified mails are {incorrectly_classified}')

 
print(f'classifer\'s accuracy = {100*classifier.score(x_test,y_test)}%')
