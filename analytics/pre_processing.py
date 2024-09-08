import json
import re
from bs4 import BeautifulSoup
from langdetect import detect, LangDetectException

input_files = ['data/youtube-hatespeech.comments-andrew.json', 'data/youtube-hatespeech.comments-impaulsive.json', 'data/youtube-hatespeech.comments-lex.json', 'data/youtube-hatespeech.comments.json']
output_files = ['processed/andrew_processed.json', 'processed/impaulsive_processed.json', 'processed/lex_processed.json', 'processed/comments_processed.json']

def clean_comment(comment):
    comment = re.sub(r'http\S+|www\S+|https\S+', '', comment, flags=re.MULTILINE)
    comment = comment.replace('\r', ' ')
    comment = BeautifulSoup(comment, 'html.parser').text
    comment = re.sub(r'[^\w\s]', '', comment)
    if len(comment) > 500:
        comment = comment[:500]
    return comment

def is_english(comment):
    try:
        return detect(comment) == 'en'
    except LangDetectException:
        return False

def process_files(input_files, output_files):
    for input_file, output_file in zip(input_files, output_files):
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        unique_comments = set()  # Set to store unique commentIds
        processed_data = []

        for entry in data:
            comment_id = entry.get('commentId')
            comment = entry.get('comment')

            if comment_id and comment_id not in unique_comments and comment and is_english(comment):
                unique_comments.add(comment_id)
                entry['comment'] = clean_comment(comment)
                processed_data.append(entry)

        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(processed_data, file, indent=4)

process_files(input_files, output_files)
