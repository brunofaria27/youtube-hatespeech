import pandas as pd
import matplotlib.pyplot as plt

files_all = [
    'processed/andrew_processed_prediction.csv',
    'processed/impaulsive_processed_prediction.csv',
    'processed/lex_processed_prediction.csv'
]

def calculate_metrics(files):
    total_comments = 0
    total_replies = 0
    total_original_comments = 0
    
    file_names = []
    replies_list = []
    original_comments_list = []
    total_comments_list = []
    reply_ratio_list = []
    
    for file in files:
        df = pd.read_csv(file)
        
        total_comments += len(df)
        
        original_comments = df[~df['commentId'].str.contains(r'\.')]
        total_original_comments += len(original_comments)
        
        replies = df[df['commentId'].str.contains(r'\.')]
        total_replies += len(replies)
        
        file_names.append(file.split('/')[-1])
        replies_list.append(len(replies))
        original_comments_list.append(len(original_comments))
        total_comments_list.append(len(df))
        reply_ratio_list.append(len(replies) / len(original_comments) if len(original_comments) > 0 else 0)
    
    plot_metrics(file_names, replies_list, original_comments_list, total_comments_list, reply_ratio_list)
    
    metrics_df = pd.DataFrame({
        'File Name': file_names,
        'Total Comments': total_comments_list,
        'Original Comments': original_comments_list,
        'Replies': replies_list,
        'Reply Ratio': reply_ratio_list
    })
    
    print("Metrics Table:")
    print(metrics_df)
    
    return metrics_df

def plot_metrics(file_names, replies_list, original_comments_list, total_comments_list, reply_ratio_list):
    fig, ax = plt.subplots(2, 1, figsize=(10, 10))
    
    ax[0].bar(file_names, total_comments_list, color='blue', label='Total Comments')
    ax[0].bar(file_names, replies_list, color='orange', label='Replies')
    ax[0].set_title('Total Comments vs Replies')
    ax[0].legend()
    ax[0].set_ylabel('Number of Comments')
    
    ax[1].bar(file_names, reply_ratio_list, color='green', label='Reply Ratio')
    ax[1].set_title('Reply Ratio per Original Comment')
    ax[1].set_ylabel('Ratio')
    ax[1].legend()

    plt.tight_layout()
    plt.show()

metrics_df = calculate_metrics(files_all)
