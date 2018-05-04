## -*- coding: utf-8 -*-
import sys
strike_char = "-"

with open('words.txt') as f:
    words = f.read().splitlines()

def handle(input):
    input = input.lower()
    output = []
    for word in words:
        pos_list = [-1]
        for char in word:
            try:
                pos_list.append(input.index(char,pos_list[-1]+1))
            except ValueError:
                pass
        pos_list = pos_list[1:]
        if sorted(pos_list) == pos_list and len(pos_list) == len(word):
            pos_list = shift(input, pos_list)
            string = get_strike_chars(len(input))
            temp = input
            while " " in temp:
                string = set_char_at(string, temp.find(" "), " ")
                temp = set_char_at(temp, temp.find(" "), "_")
            for char, pos in zip(word, pos_list):
                string = set_char_at(string, pos, char)
            output.append(string + "   " + word)
    return output

def shift(text, pos_list):
    for i in range(len(pos_list)-1):
        okay = True
        while okay:
            char = text[pos_list[i]]
            try:
                new_pos = text.index(char, pos_list[i]+1)
            except ValueError:
                okay = False
            else:
                if new_pos < pos_list[i+1]:
                    pos_list[i] = new_pos
                else:
                    okay = False
    return pos_list

def set_char_at(string, pos, char):
    return string[:pos] + char + string[pos+1:]

def get_strike_chars(n):
    string = ""
    for i in range(n):
        string += strike_char
    return string
