import os
import csv
import re


paragraph_input_csv = os.path.join( "Resources", "paragraph_2.txt")

sentence_brk = []
total_sentences = 0

word_brk = []
total_words = 0

char_brk = [] 
char_cnt = []
total_chars = 0

avg_letter_count = 0
avg_sentence_len = 0 

with open(paragraph_input_csv, newline="") as csvfile:
    paragraph = csvfile.read().rstrip("\n")


sentence_brk = paragraph.split(".")
total_sentences = len(sentence_brk)

word_brk = re.split("[, \-!?:]+",paragraph)
total_words = len(word_brk)

for word in word_brk:
    char_cnt.append(len(word))
    total_chars = total_chars + int(len(word))

avg_letter_count =  total_chars /  total_words
avg_sentence_len =  total_words / total_sentences

print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(total_words))
print("Approximate Sentence Count: " + str(total_sentences))
print("Average Letter Count: " + str(avg_letter_count))
print("Average Sentence Length: " +str(avg_sentence_len))
