import json
import re
from bs4 import BeautifulSoup

input_files = ['data/youtube-hatespeech.comments-andrew.json', 'data/youtube-hatespeech.comments-impaulsive.json', 'data/youtube-hatespeech.comments-lex.json', 'data/youtube-hatespeech.comments.json']
output_files = ['andrew_processed_3.json', 'impaulsive_processed_3.json', 'lex_processed_3.json', 'comments_processed_3.json']

def clean_comment(comment):
    comment = re.sub(r'http\S+|www\S+|https\S+', '', comment, flags=re.MULTILINE)
    comment = BeautifulSoup(comment, 'html.parser').text
    comment = re.sub(r'[^\w\s]', '', comment)
    if len(comment) > 500:
        comment = comment[:500]
    return comment

def process_files(input_files, output_files):
    for input_file, output_file in zip(input_files, output_files):
        # Open JSON file and load as a list of JSON objects
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        for entry in data:
            if 'comment' in entry:
                entry['comment'] = clean_comment(entry['comment'])
        
        # Save the processed JSON file
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

process_files(input_files, output_files)
