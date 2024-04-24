package youtube.analytics;

import youtube.analytics.repository.MongoDBInsertion;
import youtube.analytics.repository.MongoDBRepository;
import youtube.analytics.util.YouTubeDataFetcher;

import java.io.IOException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        try {
            String videoId = "RcYjXbSJBN8";
            List<Object> comments = YouTubeDataFetcher.fetchVideoComments(videoId);

            MongoDBRepository mongoDBRepository = new MongoDBRepository();
            mongoDBRepository.connect();

            MongoDBInsertion insertion = new MongoDBInsertion(mongoDBRepository.getCollectionComments());
            
            for (Object comment : comments) {
                insertion.insertDocument(comment);
            }

            mongoDBRepository.disconnect();
            
            System.out.println("Data successfully inserted into the database.");
        } catch (IOException e) {
            System.err.println("Error retrieving video comments: " + e.getMessage());
        }
    }
}
