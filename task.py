###
from bs4 import BeautifulSoup
import requests
import pandas as pd

# read html
df = {

    "genesis":42,
    "exodus":43,
}

url_base = "https://biblehub.com/questions/{0}/{1}.htm"

def get_questions(current_book, current_chapter):

    current_url = url_base.format(current_book, current_chapter)

    r = requests.get(current_url)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    el = soup.find("p")  # Find <p>

    # print(el)
    textA = " ".join(el.strings)
    print("Text A: {0}".format(textA))
    text = " ".join(el.strip() for el in el.strings)
    print("Text: {0}".format(text))

    #Find the questions numbers in the html
    index1 = text.find('1.')
    index2 = text.find('2.')
    index3 = text.find('3.')
    index4 = text.find('4.')
    index5 = text.find('5.')
    index6 = text.find('6.')
    index7 = text.find('7.')
    index8 = text.find('8.')
    index9 = text.find('9.')
    index10 = text.find('10.')
    index11 = text.find('11.')
    index12 = text.find('12.')
    index13 = text.find('13.')
    index14 = text.find('14.')
    index15 = text.find('15.')
    index16 = text.find('16.')
    index17 = text.find('17.')
    index18 = text.find('18.')
    index19 = text.find('19.')
    index20 = text.find('20.')

    #Use the position to strip the questions 1-20
    question_1 = text[index1:index2]
    question_2 = text[index2:index3]
    question_3 = text[index3:index4]
    question_4 = text[index4:index5]
    question_5 = text[index5:index6]
    question_6 = text[index6:index7]
    question_7 = text[index7:index8]
    question_8 = text[index8:index9]
    question_9 = text[index9:index10]
    question_10 = text[index10:index11]
    question_11 = text[index11:index12]
    question_12 = text[index12:index13]
    question_13 = text[index13:index14]
    question_14 = text[index14:index15]
    question_15 = text[index15:index16]
    question_16 = text[index16:index17]
    question_17 = text[index17:index18]
    question_18 = text[index18:index19]
    question_19 = text[index19:index20]
    question_20 = text[index20:]

    question_list = [question_1, question_2, question_3, question_4, question_5,
                     question_6, question_7, question_8, question_9, question_10,
                     question_11, question_12, question_13, question_14, question_15,
                     question_16, question_17, question_18, question_19, question_20
                     ]

    return question_list

def get_input():
    try:
        get_book = input("Which book?: ")
        get_book = get_book.lower()

        get_chapter = input("Which chapter?: ")
        get_chapter = int(get_chapter) - 1

        print(get_questions(get_book,get_chapter))
    except Exception as e:
        print("error at input stage: ", e)

get_input()

