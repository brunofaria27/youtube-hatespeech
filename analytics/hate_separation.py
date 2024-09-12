import csv

input_file = 'processed/andrew_processed_prediction.csv'
output_file = 'processed/hate_comments_andrew.csv'

with open(input_file, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as out_csv_file:
        fieldnames = ['file_name', 'commentId', 'comment', 'author', 'likeCount', 'isReply', 'prediction']
        csv_writer = csv.DictWriter(out_csv_file, fieldnames=fieldnames)
        
        csv_writer.writeheader()
        
        for row in csv_reader:
            if row['prediction'] in ['offensive', 'hate speech']:
                csv_writer.writerow({
                    'file_name': row['file_name'],
                    'commentId': row['commentId'],
                    'comment': row['comment'],
                    'author': row['author'],
                    'likeCount': row['likeCount'],
                    'isReply': row['isReply'],
                    'prediction': row['prediction']
                })

print(f"File {output_file} generate with success.")
