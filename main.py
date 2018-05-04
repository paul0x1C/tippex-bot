## -*- coding: utf-8 -*-

strike_char = "#"

with open('words.txt') as f:
    words = f.read().splitlines()

def handle(que, option="", word=""):
    if que == "":
        print(option)
    else:
        if word == "hell##":
            print("yes: " + que)

        # if any(replace(word + que[0]) in s for s in words): #could be completed to a valid word with next char in que

        if possible(que, word): #could be completed to a valid word with next char in que
            handle(que[1:], option, word + que[0])
        else:
            handle(que[1:], option, word + strike_char)

            # handle(que[1:], option + get_strike_chars(len(word)), "")

        if replace(word) in words: #finished word
            handle(que[1:], option + "|" + word, "") # go on with the rest and a empty word

def replace(string):
    string = string.replace(strike_char, "")
    string = string.replace(" ", "")
    return string

def possible(que, word):
    for w in words:
        p = False
        if replace(word) in w:
            p = True
            for c in w[len(replace(word)):]:
                if not c in que:
                    p = False
        if p:
            return True


def get_strike_chars(n):
    chars = ""
    for i in range(n):
        chars += strike_char
    return chars

handle("hellxxworld ")
