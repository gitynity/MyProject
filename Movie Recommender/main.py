#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk


#Getting input from the csv file using pandas read_csv()

window = Tk()		#GUI window starts
window.title("Movie Recommendation App")
window.geometry('500x1000')
df = pd.read_csv(r'C:\Users\nns\Desktop\ML Project\Building Movie Recommendation System using ML\movie_recommender\stats_of_movies.csv')

df["title"] = df["title"].str.lower()	#converting movie name in dataframe to lowercase so that it is easier to match against the user input

#Features Selection for our model

features = ['keywords', 'genres', 'cast', 'director', 'popularity', 'vote_average']

#Creating a column in DataFrame which combines all the selected features for our model

for feature in features:
  df[feature] = str(df[feature])	#typecasting the feature to str so that it is easy to concatenate into one coloumn

def featuresForModel(row):		#function for concatenation of features
  return row['keywords'] + " " + row['genres'] + " " + row['cast'] + " " + row['director'] + " " + row['popularity'] + " " + row['vote_average']

df['featuresForOurModel'] = df.apply(featuresForModel, axis = 1)	#concatenation applied on each row

#Calculating the count matrix from this new combined column

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['featuresForOurModel'])

#Computing the Cosine Similarity based on the count_matrix

cs = cosine_similarity(count_matrix)


window.withdraw()

USER_INP = simpledialog.askstring(title="Input",prompt="Enter the full name of a movie you like:")		#taking input from the user in GUI window

movie_user_likes = USER_INP

#Get index of this movie from its title


def find_index_by_movie(title):		#returns the movie index from dataframe for a given movie title
  return df[df.title == title]["index"].values[0]


movie_position = find_index_by_movie(movie_user_likes)

similar_movies = list(enumerate(cs[movie_position]))	#enumeration of similar movies for the purpose of sorting

Recommendations = sorted(similar_movies, key = lambda x: x[1], reverse = True)	#sorting of similar movies in descending order based on their similarity level

def find_movie_by_index(index):		#returns the movie title from dataframe for a given movie index
  return df[df.index == index]["title"].values[0]

i = 0
my_list = []
for movie in Recommendations:
  my_list.append(find_movie_by_index(movie[0]))
  i += 1
  if i == 50:
	  break
my_list.pop(0)
ans = '\n'.join(my_list)

window.deiconify()
label1 = Label(window,text=ans)			#list of recommended movies in GUI window
label1.config(font=("Courier", 10))
label1.pack()

window.mainloop()
