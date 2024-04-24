package youtube.analytics.repository;

import io.github.cdimascio.dotenv.Dotenv;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.MongoCollection;
import org.bson.Document;

public class MongoDBRepository {
    private String URI;
    private static final String database = "youtube-hatespeech";
    private MongoClient mongoClient;
    private MongoDatabase mongoDatabase;

    public MongoDBRepository() {
        Dotenv dotenv = Dotenv.configure().load();
        URI = dotenv.get("URI");
    }

    public String getURI() {
        return URI;
    }

    public static String getDatabase() {
        return database;
    }

    public void connect() {
        mongoClient = MongoClients.create(getURI());
        mongoDatabase = mongoClient.getDatabase(getDatabase());
    }

    public void disconnect() {
        if (mongoClient != null) {
            mongoClient.close();
        }
    }

    public MongoCollection<Document> getCollectionComments() {
        return mongoDatabase.getCollection("comments");
    }
}
