###
from bs4 import BeautifulSoup
import requests

df = {
    "genesis":50,
    "exodus":40,
    "leviticus":27,
    "numbers":36,
    "deuteronomy":34,
    "joshua":24,
    "judges":21,
    "ruth":4,
    "1 samuel":31,
    "2 samuel":24,
    "1 kings":22,
    "2 kings":25,
    "1 chronicles":29,
    "2 chronicles":36,
    "ezra":10,
    "nehemiah":13,
    "esther":10,
    "job":42,
    "psalms":150,
    "proverbs":31,
    "ecclesiastes":12,
    "song of solomon":8,
    "isaiah":66,
    "jeremiah":52,
    "lamentations":5,
    "ezekiel":48,
    "daniel":12,
    "hosea":14,
    "joel":3,
    "amos":9,
    "obadiah":1,
    "jonah":4,
    "micah":7,
    "nahum":3,
    "habakkuk":3,
    "zephaniah":3,
    "haggai":2,
    "zechariah":14,
    "malachi":4,
    "matthew":28,
    "mark":16,
    "luke":24,
    "john":21,
    "acts":18,
    "romans":16,
    "1 corinthians":16,
    "2 corinthians":13,
    "galatians":6,
    "ephesians":6,
    "philippians":4,
    "colossians":4,
    "1 thessalonians":5,
    "2 thessalonians":3,
    "1 timothy":6,
    "2 timothy":4,
    "titus":3,
    "philemon":1,
    "hebrews":13,
    "james":5,
    "1 peter":5,
    "2 peter":3,
    "1 john":5,
    "2 john":1,
    "3 john":1,
    "jude":1,
    "revelation":22
    }

url_base_niv_book = "https://biblehub.com/niv/{0}/{1}.htm"
url_base_questions = "https://biblehub.com/questions/{0}/{1}.htm"

def get_input():
    try:
        get_book = input("Which book?: ")
        get_book = get_book.lower()
        get_book = get_book.strip()  # remove trailing spaces

        if get_book not in df.keys():
            print("{0} not in list of books".format(get_book))
            print("please enter one of the following: {0}".format(df.keys()))
            quit()

        get_book_replace_spaces = get_book.replace(" ", "_") #replace the spaces with _.
        print(get_book_replace_spaces)

        get_chapter = input("Which chapter?: ")
        get_chapter = int(get_chapter)
        max_chapter = int(df.get(get_book))

        if get_chapter > max_chapter:
            print("maximum chapter for {0} is {1}".format(get_book, max_chapter))
            get_chapter = max_chapter

        get_question_count = input("How many questions (1-20)?: ")
        get_question_count = int(get_question_count)
        if get_question_count < 0:
            get_question_count = 1
        if get_question_count > 20:
            get_question_count = 20

    except Exception as e:
        print("error at input stage: ", e)

    return [get_book, get_book_replace_spaces, get_chapter, get_question_count]


def get_niv_chapter(current_book, current_chapter):

    current_url = url_base_niv_book.format(current_book, current_chapter)

    r = requests.get(current_url)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')

    # get title
    title = soup.find("p")  # Find <p>
    #title_string = " ".join(title.strings)
    title_string = " ".join(title.strip() for title in title.strings)
    intro_text = "\n{0} {1} bible study - {2}!:".format(current_book, current_chapter, title_string)
    print(intro_text.upper(), "\n")

    # get verses
    verses = soup.find(class_='chap') #find_all
    verses_string_new_line = " ".join(verses.strings)
    print(verses_string_new_line)

def get_questions(current_book, current_chapter):

    current_url = url_base_questions.format(current_book, current_chapter)

    r = requests.get(current_url)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    el = soup.find("p")  # Find <p>
    text = " ".join(el.strip() for el in el.strings) #textA = " ".join(el.strings)

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


def print_questions(get_book, get_book_replace_spaces, get_chapter, get_question_count):

    question_list = get_questions(get_book_replace_spaces, get_chapter)

    title = ("\n{0} {1} bible study questions!:".format(get_book, get_chapter))
    print(title.upper())

    for i in range(0, get_question_count):
        print(question_list[i])



get_input()

