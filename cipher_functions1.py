"""Starter for CSC108 Assignment 2"""

from typing import List, TextIO

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions here:   

def clean_message(message: str) -> str:
    """
    Return a copy of message that includes only its alphabetic characters, 
    where each of those characters has been converted to uppercase.
    
    preconditions: this function only works for the 26 English alphabets
    
    >>> clean_message('12312312Aaaabb')
    'AAAABB'
    >>> clean_message('12312312A *(*(*^aaabb')
    'AAAABB'
    """
    result = ''
    for i in message:
        if i.isalpha():
            result = result + i.upper()
    return result


def encrypt_letter(letter: str, keystream_value: int) -> str:
    """
    Apply the keystream value to the letter to encrypt the letter, 
    and return the letter after encryption.
    letter represents a single uppercase letter and keystream_value
    represents a keystream value.
    
    preconditions: This function only works for the 26 English alphabets.
    
    >>> encrypt_letter('H', 7)
    'O'
    >>> encrypt_letter('O', 17)
    'F'
    """
    a = ord(letter) - 64 + keystream_value
    if a > 26:
        a = a - 26
    a = a % 26
    result = chr(a + 64)
    if result == '@':
        return 'Z'
    else:
        return result


def decrypt_letter(letter: str, keystream_value: int) -> str:
    """
    Apply the keystream value to the letter to decrypt the letter, 
    and return the letter after decryption.
    letter represents a single uppercase letter 
    and keystream_value represents a keystream value.

    preconditions: This function only works for the 26 English alphabet.
    
    >>> decrypt_letter('O',7)
    'H'
    >>> decrypt_letter('F',17)
    'O'
    """
    a = ord(letter) - 64 - keystream_value
    if a < 0:
        a = a + 26
    a = a % 26
    result = chr(a + 64)
    if result == '@':
        return 'Z'
    else:
        return result    


def swap_cards(card_deck: List[int], index: int) -> None:
    """
    Swap the card at the index with the card that follows it. 
    Treat the deck as circular: if the card at the index is on the 
    bottom of the deck, swap that card with the top card.
    this function doesn't return anything. The deck is to be mutated.
    card_deck represents a deck of cards 
    and index represents an index into the deck.
    
    preconditions: card_deck is not empty, and index is a valid position
    
    >>> a = [1,2,3,4,5,6,7]
    >>> swap_cards(a, 3)
    >>> a 
    [1, 2, 3, 5, 4, 6, 7]
    
    >>> a = [1,2,3,4,5,6,7]
    >>> swap_cards(a, 6)
    >>> a
    [7, 2, 3, 4, 5, 6, 1]
    """
    if index != len(card_deck) - 1:
        intermediary = card_deck[index]
        card_deck[index] = card_deck[index + 1]
        card_deck[index + 1] = intermediary
    else:
        intermediary = card_deck[index]
        card_deck[index] = card_deck[0]
        card_deck[0] = intermediary      
        

def get_small_joker_value(card_deck: List[int]) -> int:
    """
    Return the value of the small joker 
    (value of the second highest card) for the given deck of cards.
    card_deck refers to card deck.
    
    preconditions: card_deck is not empty
    
    >>> get_small_joker_value([1,2,3,4,5,6,7,8,9])
    8
    >>> get_small_joker_value([1,288,2,33,5,6,11])
    33
    """
    big_joker = 0
    small_joker = 0
    for card_value in card_deck:
        if card_value > big_joker:
            small_joker = big_joker
            big_joker = card_value
        elif card_value > small_joker:
            small_joker = card_value
    return small_joker
    

def get_big_joker_value(card_deck: List[int]) -> int:
    """
    Return the value of the big joker 
    (value of the highest card) for the given deck of cards.
    card_deck refers to card deck.
    
    preconditions: card_deck is not empty
    
    >>> get_big_joker_value([1,2,3,4,5,6,7,8,9])
    9
    >>> get_big_joker_value([1,288,2,33,5,6,11])
    288
    """
    big_joker = 0
    for card_value in card_deck:
        if card_value > big_joker:
            big_joker = card_value
    return big_joker    


def move_small_joker(card_deck: List[int]) -> None:
    """
    Swap the small joker with the card that follows it but return nothing
    card_deck refers to card deck
    
    preconditions: card_deck is not empty
    
    >>> a = [1111,2,3,0,2000,1222]
    >>> move_small_joker(a)
    >>> a
    [1222, 2, 3, 0, 2000, 1111]
    
    >>> a = [1,2,3,5,7,9,10]
    >>> move_small_joker(a)
    >>> a
    [1, 2, 3, 5, 7, 10, 9]
    """
    big_joker = 0
    small_joker = 0
    big_joker_index = 0
    small_joker_index = 0
    for card_index in range(len(card_deck)):
        if card_deck[card_index] > big_joker:
            small_joker = big_joker
            big_joker = card_deck[card_index]
            small_joker_index = big_joker_index
            big_joker_index = card_index
        elif card_deck[card_index] > small_joker:
            small_joker = card_deck[card_index]
            small_joker_index = card_index
    swap_cards(card_deck, small_joker_index)


def move_big_joker(card_deck: List[int]) -> None:
    """
    Swap the big joker with the card that follows it but return nothing
    card_deck refers to card deck
    
    preconditions: card_deck is not empty
    
    >>> a = [4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12]
    >>> move_big_joker(a)
    >>> a
    [4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, 9, 12]
    
    >>> a = [1, 4, 7, 10, 13, 16, 22, 25, 3, 6, 9, 12, 28]
    >>> move_big_joker(a)
    >>> a
    [4, 28, 7, 10, 13, 16, 22, 25, 3, 6, 9, 12, 1]
    """
    big_joker = 0
    big_joker_index = 0
    for card_index in range(len(card_deck)):
        if card_deck[card_index] > big_joker:
            big_joker = card_deck[card_index]
            big_joker_index = card_index
    swap_cards(card_deck, big_joker_index)
    if big_joker_index == len(card_deck) - 1:
        big_joker_index = -1
    swap_cards(card_deck, big_joker_index + 1)


def triple_cut(card_deck: List[int]) -> None:
    """
    switch the part of card_deck on the left of big joker 
    and the part of card_deck on the right of small joker
    but return nothing
    card_deck refers to card deck
    
    preconditions: card_deck is not empty
    
    >>> a = [1,5,77,1,2,3,4,5,6,10,4]
    >>> triple_cut(a)
    >>> a
    [4, 77, 1, 2, 3, 4, 5, 6, 10, 1, 5]
    
    >>> a = [1,5,77,1,2,3,4,5,6,4,10]
    >>> triple_cut(a)
    >>> a
    [77, 1, 2, 3, 4, 5, 6, 4, 10, 1, 5]
    """
    big_joker = get_big_joker_value(card_deck)
    small_joker = get_small_joker_value(card_deck)
    for index in range(len(card_deck)):
        if card_deck[index] == big_joker:
            first = index
        if card_deck[index] == small_joker:
            second = index
    if first > second:
        intermediary = first
        first = second
        second = intermediary
    new = card_deck[second + 1:] + card_deck[first : second + 1]
    new = new + card_deck[0:first]
    del card_deck[:]
    card_deck.extend(new)


def insert_top_to_bottom(card_deck: List[int]) -> None:
    """
    Examine the value of the bottom card of the deck; 
    move that many cards from the top of the deck to the bottom, 
    inserting them just above the bottom card.
    Special case: if the bottom card is the big joker, 
    use the value of the small joker as the number of cards.
    card_deck refers to card deck
    
    preconditions: card_deck is not empty
    
    >>> a = [1,2,5,100,2,555,22,3]
    >>> insert_top_to_bottom(a)
    >>> a
    [100, 2, 555, 22, 1, 2, 5, 3]
    
    >>> a = [1,2,5,3,2,0,2,10] 
    >>> insert_top_to_bottom(a)
    >>> a
    [0, 2, 1, 2, 5, 3, 2, 10]
    """
    big_joker = get_big_joker_value(card_deck)
    if big_joker != card_deck[-1]:  
        slice_part = card_deck[0 : card_deck[-1]]
        middle = card_deck[card_deck[-1] : -1]
        last = [card_deck[-1]]
        del card_deck[:]
        card_deck.extend(middle + slice_part + last)
    else:
        index = get_small_joker_value(card_deck)    
        slice_part = card_deck[0 : index]
        middle = card_deck[index : -1]
        last = [card_deck[-1]]
        del card_deck[:]
        card_deck.extend(middle + slice_part + last) 


def get_card_at_top_index(card_deck: List[int]) -> int:
    """
    Using the value of the top card as an index,
    return the card in the deck at that index.
    if the top card is the big joker, use the value of 
    the small joker as the index.
    
    precondition: card_deck is not empty
    
    >>> get_card_at_top_index([1,10,11,2,5,1,1,2,5,1,2,9,1])
    10
    >>> get_card_at_top_index([23,10,11,2,5,1,1,2,5,1,2,9,1])
    9
    """
    small_joker = get_small_joker_value(card_deck)
    big_joker = get_big_joker_value(card_deck)
    if card_deck[0] == big_joker:
        w = small_joker
    else:
        w = card_deck[0]
    return(card_deck[w])


def get_next_keystream_value(card_deck: List[int]) -> int:
    """
    Repeat all five steps of the algorithm until a valid 
    keystream value is produced, then return that valid keystream value.
    card_deck refers to card deck
    
    preconditions: card_deck is not empty
    
    >>> a = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5,8,11,14,17,20,23,26]
    >>> get_next_keystream_value(a)
    11
    
    >>> get_next_keystream_value([1,4,5,10,3,6,8,2,9,0,2])
    4
    """
    small_joker = get_small_joker_value(card_deck)
    big_joker = get_big_joker_value(card_deck)    
    while 1 == 1:
        move_small_joker(card_deck)
        move_big_joker(card_deck)
        triple_cut(card_deck)
        insert_top_to_bottom(card_deck)
        key = get_card_at_top_index(card_deck)
        if key != small_joker and key != big_joker:
            return key
    return None   


def process_messages(c_deck: List[int], m: List[str], inst: str) -> List[str]:
    """
    Return a list of encrypted messages if the third parameter is 
    ENCRYPT or decrypted messages if the third parameter is DECRYPT. 
    The messages are returned in the same order as they are given. 
    Note that the first parameter may also be mutated during a function call. 
    c_deck refers to card deck, m refers to message and inst refers to
    instruction "Encrypt" or "Decrypt"
    
    
    preconditions: c_deck, m and inst are not empty
    
    >>> a = ['abd  e22@#!','1212ddas22','22222']
    >>> process_messages([1,2,5,9,2,3,8,1,4,5],a,'e')
    ['CCEH', 'FIDX', '']
    
    >>> a = ['abd  e22@#!','1212ddas22','22222']
    >>> s = process_messages([1,2,5,9,2,3,8,1,4,5],a,'e')
    >>> process_messages([1,2,5,9,2,3,8,1,4,5],s,'d')
    ['ABDE', 'DDAS', '']
    """
    new_m = []
    for index in range(len(m)):
        m[index] = clean_message(m[index])
    if inst == ENCRYPT:
        for i1 in m:
            s = ''
            for i2 in i1:
                s += encrypt_letter(i2, get_next_keystream_value(c_deck))
            new_m.append(s)
        return new_m
    elif inst == DECRYPT:
        for i1 in m:
            s = ''
            for i2 in i1:
                s += decrypt_letter(i2, get_next_keystream_value(c_deck))
            new_m.append(s)
        return new_m
    return None


def read_messages(file_for_reading: TextIO) -> List[str]:
    """
    Read and return the contents of the file as a list of messages, 
    in the order in which they appear in the file. Strip the newline from 
    each line. The list should be the same length as the number of lines 
    in the file.
    """
    paragraph = file_for_reading.readlines()
    for index in range(len(paragraph)):
        paragraph[index] = paragraph[index].rstrip('\n')
    return paragraph


def is_valid_deck(card_deck: List[int]) -> bool:
    """
    Return True if and only if the candidate deck is a valid deck of cards. 
    A valid deck contains every integer from 1 
    up to the number of cards in the deck. 
    
    preconditions: card_deck is not empty

    >>> is_valid_deck([5,2,4,3,1,6,7,8])
    True
    >>> is_valid_deck([1,2,3,4,5,6,7,8,0])
    False
    """
    for index in range(len(card_deck)):
        if not (index + 1 in card_deck):
            return False
    return True


def read_deck(file_for_reading: TextIO) -> List[int]:
    """
    Read and return the numbers that are in the file, 
    in the order in which they appear in the file. 
    Return the deck in the form of list of int
    """
    card_deck = file_for_reading.read()
    card_deck = card_deck + ' '
    num = ''
    result = []
    for item in card_deck:
        if item.isdigit():
            num = num + item
        else:
            if not num == '':
                result.append(int(num))
            num = ''
    return result
            


if __name__ == '__main__':
    
    """Optional: uncomment the lines import doctest and doctest.testmod() to 
    have your docstring examples run when you run cipher_functions.py
    NOTE: your docstrings MUST be properly formatted for this to work!
    """
    
    import doctest
    doctest.testmod()
