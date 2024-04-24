package youtube.analytics.util;

import youtube.analytics.model.MainComment;
import youtube.analytics.model.ReplyComment;

import java.io.IOException;
import java.util.List;

public class YouTubeDataFetcher {
    private String API_KEY;

    public String getAPI_KEY() {
        return API_KEY;
    }

    public void setAPI_KEY(String API_KEY_GOOGLE) {
        API_KEY = API_KEY_GOOGLE;
    }
    
    public static List<MainComment> fetchVideoComments(String videoId) throws IOException {
        return null;
    }

    private static List<ReplyComment> fetchRepliesForComment(String commentId) throws IOException {
        return null;
    }
}
