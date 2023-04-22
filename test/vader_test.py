from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from openpyxl.workbook import Workbook
from textblob import TextBlob
import xlsxwriter
import matplotlib.pyplot as plt
import datetime
import os

def createGraph(hoja2, carpeta):
    labels = 'Positives', 'Negatives', 'Neutrals'
    sizes = [hoja2[0].get("Positive"), hoja2[0].get("Negative"), hoja2[0].get("Neutral")]
    
    explode = (0, 0.1, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.savefig(carpeta+"/"+"graph.png")

def main():

    # Dia y hora actual para nombre de carpeta
    now = datetime.datetime.now()
    # cambiar formato de fecha
    ea = now.strftime("%Y-%m-%d_%H-%M-%S")
    carpeta = "comments_" + ea
    os.mkdir("./"+carpeta)

    # sentences = array de Pedro

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

    # Variables
    analyzer = SentimentIntensityAnalyzer()
    hoja1 = []
    positive, negative, neutral = 0, 0, 0

    # Hoja 1
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
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

    # Hoja 2
    hoja2 = []
    hoja2.append({"Positive": positive, "Negative": negative, "Neutral": neutral})
    createGraph(hoja2, carpeta)

    # Hoja 3
    hoja3 = []
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
        if vs.get("pos") >= 0.85:
            testimonial = TextBlob(sentence)
            hoja3.append({"sentence":sentence, "neg": vs.get("neg"), "neu": vs.get("neu"), "pos": vs.get("pos"), "compound": vs.get("compound")})
        elif vs.get("neg") >= 0.85:
            testimonial = TextBlob(sentence)
            hoja3.append({"sentence":sentence, "neg": vs.get("neg"), "neu": vs.get("neu"), "pos": vs.get("pos"), "compound": vs.get("compound")})
        
    # Si hoja3 esta vacia
    if not hoja3:
        hoja3.append({"sentence":"No hay oraciones con un sentimiento extremo", "neg": 0, "neu": 0, "pos": 0, "compound": 0})

    # Creación de Pandas.
    df1 = pd.DataFrame(hoja1)
    df2 = pd.DataFrame(hoja2)
    df3 = pd.DataFrame(hoja3)

    # Crear el Excel
    writer = pd.ExcelWriter(carpeta+"/"+'infoComments.xlsx', engine='xlsxwriter')

    # Asignar las hojas
    df1.to_excel(writer, sheet_name='Hoja1', index=False)
    df2.to_excel(writer, sheet_name='Hoja2', index=False)
    df3.to_excel(writer, sheet_name='Hoja3', index=False)

    # Cerramos el Excel
    writer.close()


if __name__ == '__main__':
    main()