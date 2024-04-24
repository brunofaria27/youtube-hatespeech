package youtube.analytics.util;

import io.github.cdimascio.dotenv.Dotenv;
import youtube.analytics.model.MainComment;
import youtube.analytics.model.ReplyComment;

import java.io.IOException;
import java.util.List;

public class YouTubeDataFetcher {
    private static String API_KEY;

    public YouTubeDataFetcher() {
        Dotenv dotenv = Dotenv.configure().load();
        API_KEY = dotenv.get("API_KEY");
    }

    public String getAPI_KEY() {
        return API_KEY;
    }
    
    public static List<MainComment> fetchVideoComments(String videoId) throws IOException {
        return null;
    }

    private static List<ReplyComment> fetchRepliesForComment(String commentId) throws IOException {
        return null;
    }
}
