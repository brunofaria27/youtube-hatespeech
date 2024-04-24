from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

API_KEY = "y"

def get_video_comments(video_id):
    try:
        comments_analytics = []

        youtube = build("youtube", "v3", developerKey=API_KEY)

        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=10000
        ).execute()

        while response:
            for item in response["items"]:

                comment_data = {
                    "comment_id": item["id"],
                    "comment": item["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
                    "author": item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                    "like_count": item["snippet"]["topLevelComment"]["snippet"]["likeCount"],
                    "is_reply": item["snippet"]["canReply"],
                    "reply_id": None
                }
                comments_analytics.append(comment_data)

                # Verifica se há respostas ao comentário
                if item["snippet"]["totalReplyCount"] > 0:
                    reply_response = youtube.comments().list(
                        part="snippet",
                        parentId=item["id"],
                        textFormat="plainText",
                        maxResults=100
                    ).execute()
                    for reply_item in reply_response["items"]:
                        
                        reply_data = {
                            "comment_id": reply_item["id"],
                            "comment": reply_item["snippet"]["textDisplay"],
                            "author": reply_item["snippet"]["authorDisplayName"],
                            "like_count": reply_item["snippet"]["likeCount"],
                            "is_reply": item["snippet"]["canReply"],
                            "reply_id": item["id"]
                        }
                        comments_analytics.append(reply_data)

            # Verifique se há mais comentários para recuperar
            if "nextPageToken" in response:
                response = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    textFormat="plainText",
                    maxResults=10000,
                    pageToken=response["nextPageToken"]
                ).execute()
            else:
                break

        return comments_analytics
    except HttpError as e:
        print("An HTTP error occurred %d:\n%s" % (e.resp.status, e.content))

if __name__ == "__main__":
    video_id = "x"
    all_comments = get_video_comments(video_id)
    print(json.dumps(all_comments, indent=2))