package youtube.analytics.repository;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoCollection;
import org.bson.Document;

/* https://www.mongodb.com/docs/drivers/java/sync/current/quick-start/ */
public class MongoDBRepository {
    private MongoClient mongoClient;
    private MongoCollection<Document> userCollection;
    private MongoCollection<Document> commentCollection;

    public MongoClient getMongoClient() {
        return mongoClient;
    }

    public void setMongoClient(MongoClient mongoClient) {
        this.mongoClient = mongoClient;
    }

    public MongoCollection<Document> getUserCollection() {
        return userCollection;
    }

    public void setUserCollection(MongoCollection<Document> userCollection) {
        this.userCollection = userCollection;
    }

    public MongoCollection<Document> getCommentCollection() {
        return commentCollection;
    }

    public void setCommentCollection(MongoCollection<Document> commentCollection) {
        this.commentCollection = commentCollection;
    }
}
