from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from openpyxl.workbook import Workbook
from textblob import TextBlob


# --- examples -------
sentences = ["VADER es lo peor que hay, horrible.",  # positive sentence example
             "VADER is smart, handsome, and funny!",  # punctuation emphasis handled correctly (sentiment intensity adjusted)
             "VADER is very smart, handsome, and funny.", # booster words handled correctly (sentiment intensity adjusted)
             "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
             "VADER is VERY SMART, handsome, and FUNNY!!!", # combination of signals - VADER appropriately adjusts intensity
             "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!", # booster words & punctuation make this close to ceiling for score
             "VADER is not smart, handsome, nor funny.",  # negation sentence example
             "The book was good.",  # positive sentence
             "At least it isn't a horrible book.",  # negated negative sentence with contraction
             "The book was only kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
             "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
             "Today SUX!",  # negative slang with capitalization emphasis
             "Today only kinda sux! But I'll get by, lol", # mixed sentiment example with slang and constrastive conjunction "but"
             "Make sure you :) or :D today!",  # emoticons handled
             "Catch utf-8 emoji such as such as 💘 and 💋 and 😁",  # emojis handled
             "Not bad at all"  # Capitalized negation
             ]

analyzer = SentimentIntensityAnalyzer()
hoja1 = []
hoja2 = []
positive = 0
negative = 0
neutral = 0
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    # Hoja 1
    score = 0
    if vs.get("compound") >= 0.05:
        score = "Positive"
        positive += 1
    elif vs.get("compound") > -0.05 and vs.get("compound") < 0.05:
        score = "Neutral"
        neutral += 1
    else:
        score = "Negative"
        negative += 1
    testimonial = TextBlob(sentence)
    hoja1.append({"sentence":sentence, "neg": vs.get("neg"), "neu": vs.get("neu"), "pos": vs.get("pos"), "compound": vs.get("compound"), "Polarity": testimonial.sentiment.polarity, "Subjectivity": testimonial.sentiment.subjectivity, "score": score})
    #print("{:-<65} {}".format(sentence, str(vs)))



# Hoja 2
hoja2.append({"Type": ["Positive", "Negative", "Neutral"], "Count": [positive, negative, neutral] })

# Create a Pandas dataframe from some data.
df1 = pd.DataFrame(hoja1)
df2 = pd.DataFrame(hoja2)
# create a Excel with to_excel() method

df1.to_excel('pandas_simple.xlsx', sheet_name='test', index=False, engine='openpyxl')