import math
import re
import sys
import datetime

def dis(price, discount):
    cash_off = price * discount * (0.01)
    price_new = price - cash_off
    price_new = round(price_new,2)
    return(price_new)

def stutter(word):
    #Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
    word_stutt = word[:2] + '... ' + word[:2] + '... '+ word + '?'
    return(word_stutt)

def circle_or_square(r, a):
    #Given the radius of a circle and the area of a square, return True if the circumference of the circle is greater than the square's perimeter and False if the square's perimeter is greater than the circumference of the circle.
    c = 2 * r * (3.14)
    p = math.sqrt(a) * 4
    if c > p:
        return True
    else:
        return False
    
def dna_to_rna(dna):
    rna = ''
    for char in dna:
        if char == 'A':
            rna = rna + 'U'
        elif char == 'T':
            rna = rna + 'A'
        elif char == 'G':
            rna = rna + 'C'
        elif char == 'C':
            rna = rna + 'G'
    return rna

def quadratic(a,b,c):
    if (b**2 - 4*a*c) > 0:
        return 2
    elif (b**2 - 4*a*c) == 0:
        return 1
    else:
        return 0
    
def karaca__encryption(word):
    word_new = ''
    for char in word[::-1]:
        if char == 'a':
            word_new += '0'
        elif char == 'e':
            word_new += '1'
        elif char == 'i' or char == 'o':
            word_new += '2'
        elif char == 'u':
            word_new += '3'        
        else:
            word_new += char
    word_new += 'aca'
    return word_new


def snakefill(n):
    a = n*n
    pos = 1
    snake = 1
    times = 0
    while pos < a:
        pos += snake
        snake = snake * 2
        times += 1
    return (times-1)


def start_end(S,k): 
    temp = S
    first = []

    for i in range(len(S)):
        if k in S and S[i] == k[0]:
            if k == S[i:(i+len(k))]:
                first.append(i)
            temp = S[(i-1):]
               
    for item in first:
        ans = '(' + str(item) + ', ' + str(item+len(k)-1) + ')'
        print(ans)


# divide s into part of k length and remove duplicates
def merge_the_tools(s, k):
    u = []
    u_new = []
    u = [s[i:i + k] for i in range(0, len(s), k)] # split string to parts

    for string in u:
        temp = ''
        seen = set()
        for char in string:
            if char not in seen:
                temp += char
                seen.add(char)
        u_new.append(temp)
    
    return u_new

# morse code
def morse(textIn):
    textIn = textIn.lower()
    textOut = ''
    alphanumeric = {'a':'.- ','b':'-... ','c':'-.-. ','d':'-.. ','e':'. ', 'f': '..-. ', 'g': '--. ', 'h': '.... ', 'i': '.. ', 'j': '.--- ', 'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ', 'o': '--- ', 'p': '.--. ', 'q': '--.- ', 'r': '.-. ', 's': '... ', 't': '- ', 'u': '..- ', 'v': '...- ', 'w': '.-- ', 'x': '-..- ', 'y': '-.-- ', 'z': '--.. ', '1': '.---- ', '2': '..--- ', '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ', '9': '----. ', '0': '----- ', ',' :'--..-- ',  '.':'.-.-.- ','?':'..--.. ', '/':'-..-. ', '-':'-....- ', '(':'-.--. ', ')':'-.--.- ', ' ': '/ '}
    for char in textIn:
        textOut += alphanumeric[char]
    print(textOut)

# find the odd character out between two strings of different order
def diffBetweenStr(x,y):
    odd = ''
    for char in y:
        if char not in x:
            odd = char
        elif y.count(char) > 1:
            odd = char
    print(odd)
    return odd
        
# Friday the 13th detector
def fri13(m,y):
    m = datetime.datetime.strptime(m, "%B").month
    w = datetime.date(y,m,13).weekday()
    if w == 4:
        return True
    else:
        return False
    
# encoded str parser; contains first name, last name, and id seperated by varrying number of zeros
def encodedStr(text):
    text = text.replace('0',' ')
    words = text.split()
    mydict = {'first name': words[0],'last name': words[1],'id': words[2]}
    return mydict


# shadow sentences are sentences where every word is the same length and order but without any of the same letters
def shadow(s1,s2):
        
    # check num of words
    w1 = s1.split()
    w2 = s2.split()
    if len(w1) != len(w2):
        return False

    # check word len
    for word in w1:
        if len(w1) != len(w2):
            return False
    
    # check for shared characters
    for word1, word2 in zip (w1, w2):
        for char in word1:
            if char in word2:
                return False
        
    # passes all tests    
    return True


