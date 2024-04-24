package youtube.analytics.util;

import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
import com.google.api.client.http.HttpRequestInitializer;
import com.google.api.services.youtube.YouTube;
import com.google.api.services.youtube.model.CommentThread;
import com.google.api.services.youtube.model.CommentThreadListResponse;

import io.github.cdimascio.dotenv.Dotenv;

import com.google.api.services.youtube.model.Comment;
import com.google.api.services.youtube.model.CommentListResponse;
import com.google.api.services.youtube.model.CommentSnippet;
import youtube.analytics.model.MainComment;
import youtube.analytics.model.ReplyComment;

import java.io.IOException;
import java.security.GeneralSecurityException;
import java.util.ArrayList;
import java.util.List;

public class YouTubeDataFetcher {
    private static final String APPLICATION_NAME = "YouTube Analytics";
    private static final String API_KEY;
    private static final YouTube youtube;
    static List<Object> comments = new ArrayList<>();

    static {
        Dotenv dotenv = Dotenv.configure().load();
        API_KEY = dotenv.get("API_KEY");
        youtube = getService();
    }

    private static YouTube getService() {
        try {
            return new YouTube.Builder(
                    GoogleNetHttpTransport.newTrustedTransport(),
                    com.google.api.client.json.jackson2.JacksonFactory.getDefaultInstance(),
                    new HttpRequestInitializer() {
                        public void initialize(com.google.api.client.http.HttpRequest request) throws IOException {
                        }
                    })
                    .setApplicationName(APPLICATION_NAME)
                    .build();
        } catch (GeneralSecurityException | IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static List<Object> fetchVideoComments(String videoId) throws IOException {
        YouTube.CommentThreads.List commentThreadsListRequest = youtube.commentThreads()
                .list("snippet")
                .setVideoId(videoId)
                .setMaxResults(100L)
                .setKey(API_KEY);

        String nextPageToken = null;
        do {
            commentThreadsListRequest.setPageToken(nextPageToken);
            CommentThreadListResponse response = commentThreadsListRequest.execute();

            for (CommentThread commentThread : response.getItems()) {
                CommentSnippet topLevelComment = commentThread.getSnippet().getTopLevelComment().getSnippet();

                MainComment mainComment = new MainComment();
                mainComment.setCommentId(commentThread.getId());
                mainComment.setComment(topLevelComment.getTextDisplay());
                mainComment.setAuthor(topLevelComment.getAuthorDisplayName());
                mainComment.setLikeCount(topLevelComment.getLikeCount());
                mainComment.setReply(commentThread.getSnippet().getTotalReplyCount() > 0);

                comments.add(mainComment);

                if (commentThread.getSnippet().getTotalReplyCount() > 0) {
                    fetchRepliesForComment(commentThread.getId());
                }
            }

            nextPageToken = response.getNextPageToken();
        } while (nextPageToken != null);

        return comments;
    }

    private static void fetchRepliesForComment(String commentId) throws IOException {
        YouTube.Comments.List commentsListRequest = youtube.comments()
                .list("snippet")
                .setParentId(commentId)
                .setMaxResults(100L)
                .setKey(API_KEY);

        String nextPageToken = null;
        do {
            commentsListRequest.setPageToken(nextPageToken);
            CommentListResponse response = commentsListRequest.execute();

            for (Comment comment : response.getItems()) {
                ReplyComment reply = new ReplyComment();
                reply.setCommentId(comment.getId());
                reply.setComment(comment.getSnippet().getTextDisplay());
                reply.setAuthor(comment.getSnippet().getAuthorDisplayName());
                reply.setLikeCount(comment.getSnippet().getLikeCount());
                reply.setReply(true);
                reply.setParentMainCommentId(commentId);

                comments.add(reply);
            }

            nextPageToken = response.getNextPageToken();
        } while (nextPageToken != null);
    }
}
