"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4

# Helper functions.

def first_alnum_substring(text: str) -> str:
    """Return all alphanumeric characters in text from the beginning up to the
    first non-alphanumeric character, or, if text does not contain any
    non-alphanumeric characters, up to the end of text."

    >>> first_alnum_substring('')
    ''
    >>> first_alnum_substring('IamIamIam')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!andMore')
    'iamiamiam'
    >>> first_alnum_substring('$$$money')
    ''
    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()


def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'
    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word


# Required functions

def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []
    """
    
    lst = []
    #sub_list = first_alnum_substring(lst[i])
    words = text.split(' ') #split text by spaces 
    for word in words: 
        if '@' in word[0]:
            mentions = first_alnum_substring(word[1:])
            if mentions != '':
                lst.append(mentions)
    return lst

    
def extract_hashtags(text: str) -> List[str]:
    """return a list containing all of the unique hashtags in the text, in 
    the order they appear in the text, converted to lowercase. 
    ['ilovepie', 'jujubeans', 'r2d2']
    >>> extract_hashtags('#hi #HI #Hi #pie so cute! #cute')
    ['hi', 'pie', 'cute']
    >>> extract_hashtags('@hi#cute i'm so cute #cutedogs')
    ['cute', 'cutedogs']
    """
    
    lst = []
    #sub_list = first_alnum_substring(lst[i])
    words = text.split(' ') #split text by spaces 
    for word in words: #if string contains @, append to lst
        if '#' in word[0]:
            mentions = first_alnum_substring(word[1:]) #how do i remove the @, then call fcn firstalnumsubstring
            if mentions != '' and mentions not in lst:
                lst.append(mentions)
    return lst


def count_words(text:str, d:Dict[str, int]) -> None:
    """update the counts of words in the dictionary. If a word is not the 
    dictionary yet, it should be added.
    >>>count_words('#UofT Nick by day by!', d)
    {'Nick': 1,'by': 2, 'day':1}
    >>>count_words('#UofT @iguana Nick by day hi hi by!', d)
    {'Nick': 1,'by': 2, 'day':1, 'hi': 2}
    >>>count_words('#UofT@iguana Nick by day hi hi by!', d)
    {'Nick': 1,'by': 2, 'day':1, 'hi': 2}
    """
    
    words = text.split()
    for word in words:
        if word[0] != '#' and word[0] != '@' and word[0:4] != 'http':
            word = clean_word(word)            
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return None
       

def common_words(d:Dict[str, int], N:int) -> None:
    """update the given dictionary so that it only includes the most common 
    words
    >>>d = {'cow': 12, 'boot': 1, 'hi': 22}
    common_words(d, 2)
    None
    >>>d = {'cow': 2, 'boot': 1, 'hi': 22}
    common_words(d, 22)
    None
    >>>d = {'cow': 2, 'boot': 1, 'hi': 2}
    common_words(d, 2)
    None
    """
    
    tuples = []
    for key,value in d.items():
        tuples.append((key,value))    
    tuples.sort()
    counter = 0
    while True:
        if len(d) == N:
            break
        else:
            d.pop(tuples[counter][0])
            counter += 1
    return None


def read_tweets(text:TextIO) -> Dict[str, List[tuple]]:
    """ Reads text and interprets it in a form of a tweet. 
    A tweet tuple should have the form (tweet text, date, source, 
    favourite count, retweet count)
    >>> text = open('tweets_small.txt', 'r')
    >>> read_tweets(text)
    """
    
    d = text.read().split("<<<EOT")
    dic = {}
    # d is now a list of different tweets
    for tweet in d:# make a tuple 
        text = tweet.split(',')[-1]
        text = text.split()[2:-1]# eg. date is located between the first colon and comma
        source = tweet.split(' ')[-1]
        fav_count = tweet.split(',')[-2]
        rtwt_count = tweet.split(',')[-1]
        rtwt_count = rtwt_count.split(' ')[0]
        date = tweet.split(',')[0] #(this gives me everything before first comma)
        date = date.split(':')[-1] # this is my date
        # source = ...
        tuple = (text, date, source, fav_count, rtwt_count)
        username = tweet.split(',')[0]
        username = username.split(':')[-1]
        if username in dic:
            dic[username].append(tuple)
        else:
            dic[username] = [tuple]
    return dic
    

def most_popular(d:Dict[str, int], l:List[tuple], start:int, end:int) -> str:
    """return the username of the Twitter user who was most popular on Twitter 
    between the two dates (inclusive of the start and end dates).
    >>>most_popular({'hi': 2, 'bi': 3}, (hi, 2, bi, 3), 2, 5)
    'hi bi'
    >>>most_popular({'hi': 2, 'bi': 3, 'ji': 3}, (hi, 2, bi, 3), 2, 5)
    'hi bi ji'
    >>>most_popular({'hi': 2}, (hi, 2), 1, 5)
    'hi'
    """
    
    return ''


def detect_author(d:Dict[str, int], l:List[tuple], date:str) -> str:
    """return the username (in lowercase) of the most likely author of that 
    tweet, based on the hashtags they use. If all hashtags in the tweet are 
    uniquely used by a single user, then return that user's username. 
    Otherwise, return the string 'unknown'.
    >>>detect_author({'hi': 2, 'bi': 3}, (hi, 2, bi, 3), 20181105)
    'hi'
    >>>detect_author({'hi': 2, 'bi': 3}, (hi, 2, bi, 3), 20181105)
    'bi'
    >>>detect_author({'hi': 2, 'bi': 3, 'tri': 5}, (hi, 2), 20181105)
    'hi'
    """
    
    return 'unknown'


if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()
