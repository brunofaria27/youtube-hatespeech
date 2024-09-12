import pandas as pd
import matplotlib.pyplot as plt
import os

files_all = [
    'processed/andrew_processed_prediction.csv',
    'processed/impaulsive_processed_prediction.csv',
    'processed/lex_processed_prediction.csv'
]

def calculate_metrics(files):
    total_comments = 0
    total_replies = 0
    total_original_comments = 0
    total_hate_speech_replies = 0
    
    file_names = []
    replies_list = []
    original_comments_list = []
    total_comments_list = []
    reply_ratio_list = []
    hate_speech_proportion_list = []
    
    for file in files:
        df = pd.read_csv(file)
        
        total_comments += len(df)
        
        original_comments = df[~df['commentId'].str.contains(r'\.')]
        total_original_comments += len(original_comments)
        
        replies = df[df['commentId'].str.contains(r'\.')]
        total_replies += len(replies)
        
        hate_speech_replies = replies[replies['prediction'].isin(['hate speech', 'offensive'])]
        total_hate_speech_replies += len(hate_speech_replies)
        
        file_names.append(file.split('/')[-1])
        replies_list.append(len(replies))
        original_comments_list.append(len(original_comments))
        total_comments_list.append(len(df))
        reply_ratio_list.append(len(replies) / len(original_comments) if len(original_comments) > 0 else 0)
        
        hate_speech_proportion = len(hate_speech_replies) / len(replies) if len(replies) > 0 else 0
        hate_speech_proportion_list.append(hate_speech_proportion)
    
    plot_metrics(file_names, replies_list, original_comments_list, total_comments_list, reply_ratio_list, hate_speech_proportion_list)
    
    metrics_df = pd.DataFrame({
        'File Name': file_names,
        'Total Comments': total_comments_list,
        'Original Comments': original_comments_list,
        'Replies': replies_list,
        'Reply Ratio': reply_ratio_list,
        'Hate Speech Proportion in Replies': hate_speech_proportion_list
    })
    
    print("Metrics Table:")
    print(metrics_df)
    
    return metrics_df

def plot_metrics(file_names, replies_list, original_comments_list, total_comments_list, reply_ratio_list, hate_speech_proportion_list):
    os.makedirs('graphs', exist_ok=True)
    
    # Plot Total Comments vs Replies
    fig, ax = plt.subplots()
    ax.bar(file_names, total_comments_list, color='blue', label='Total Comments')
    ax.bar(file_names, replies_list, color='orange', label='Replies')
    ax.set_title('Total Comments vs Replies')
    ax.legend()
    ax.set_ylabel('Number of Comments')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('graphs/metrics/total_comments_vs_replies.png')
    plt.close()
    
    # Plot Reply Ratio per Original Comment
    fig, ax = plt.subplots()
    ax.bar(file_names, reply_ratio_list, color='green', label='Reply Ratio')
    ax.set_title('Reply Ratio per Original Comment')
    ax.set_ylabel('Ratio')
    ax.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('graphs/metrics/reply_ratio_per_original_comment.png')
    plt.close()
    
    # Plot Hate Speech Proportion in Replies
    fig, ax = plt.subplots()
    ax.bar(file_names, hate_speech_proportion_list, color='red', label='Hate Speech Proportion')
    ax.set_title('Hate Speech Proportion in Replies')
    ax.set_ylabel('Proportion')
    ax.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('graphs/metrics/hate_speech_proportion_in_replies.png')
    plt.close()

metrics_df = calculate_metrics(files_all)
