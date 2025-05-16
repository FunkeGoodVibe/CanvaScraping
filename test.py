####
import random

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


generate_book_no = random.randint(1, 66)

print(generate_book_no)

random_book =list(df.keys())[generate_book_no]
print(random_book)

random_book_no_chapters = df[random_book]
print(random_book_no_chapters)


generate_chapter_no = random.randint(1, random_book_no_chapters)
print(generate_chapter_no)


