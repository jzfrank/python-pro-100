import pandas as pd 
import os 

if os.path.exists("data/words_to_learn.csv"):
	french_words = pd.read_csv("data/words_to_learn.csv")
else:
	french_words = pd.read_csv("data/french_words.csv")

french_dict = french_words.to_dict(orient="records")

french2english = {i['French']:i["English"] for i in french_dict}
print(len(french2english))