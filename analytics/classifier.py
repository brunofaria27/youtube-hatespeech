import json
import time
import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "Hate-speech-CNERG/bert-base-uncased-hatexplain"
device = 0 if torch.cuda.is_available() else -1  # 0 para GPU, -1 para CPU
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer, device=device)

def classify_comments_batch(comments):
    results = classifier(comments)
    return [result['label'] for result in results]

def process_files(input_files):
    for input_file in input_files:
        print(f"Processing file: {input_file}")
        start_time = time.time()

        with open(input_file, 'r') as file:
            data = json.load(file)

        comments_data = []
        processed_comments = set()

        print(f"Number of comments: {len(data)}")

        for entry in data:
            commentId = entry.get('commentId', '')
            comment = entry.get('comment', '')
            author = entry.get('author', 'Unknown')
            likeCount = entry.get('likeCount', 0)
            isReply = entry.get('isReply', False)
            
            if isinstance(likeCount, dict):
                likeCount = likeCount.get('$numberLong', 0)
            try:
                likeCount = int(likeCount)
            except ValueError:
                likeCount = 0
            
            if comment not in processed_comments:
                processed_comments.add(comment)
                
                classifications = classify_comments_batch([comment])
                
                comments_data.append({
                    'file_name': input_file,
                    'commentId': commentId,
                    'comment': comment,
                    'author': author,
                    'likeCount': likeCount,
                    'isReply': isReply,
                    'prediction': classifications[0]
                })

                df = pd.DataFrame(comments_data)
                csv_file = input_file.replace('.json', '_prediction.csv')
                df.to_csv(csv_file, index=False) 
                print(f"Processed and saved comment {commentId} to {csv_file}")

        elapsed_time = time.time() - start_time
        print(f"File {input_file} processed in {elapsed_time:.2f} seconds.")
                                                                                           #                                     X
input_files = ['processed/json/lex_processed.json'] # , 'processed/json/andrew_processed.json', 'processed/json/impaulsive_processed.json', 'processed/json/comments_processed.json']

process_files(input_files)
