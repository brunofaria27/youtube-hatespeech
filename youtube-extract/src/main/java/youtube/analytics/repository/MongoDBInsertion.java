package youtube.analytics.repository;

import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.InsertOneOptions;
import org.bson.Document;
import youtube.analytics.model.MainComment;
import youtube.analytics.model.ReplyComment;

public class MongoDBInsertion {
    private MongoCollection<Document> collection;

    public MongoDBInsertion(MongoCollection<Document> collection) {
        this.collection = collection;
    }

    public void insertDocument(Object obj) {
        if (obj instanceof MainComment) {
            MainComment mainComment = (MainComment) obj;
            insertMainComment(mainComment);
        } else if (obj instanceof ReplyComment) {
            ReplyComment replyComment = (ReplyComment) obj;
            insertReplyComment(replyComment);
        } else {
            throw new IllegalArgumentException("Object type not supported for insertion: " + obj.getClass().getName());
        }
    }

    public void insertDocument(Object obj, InsertOneOptions options) {
        if (obj instanceof MainComment) {
            MainComment mainComment = (MainComment) obj;
            insertMainComment(mainComment, options);
        } else if (obj instanceof ReplyComment) {
            ReplyComment replyComment = (ReplyComment) obj;
            insertReplyComment(replyComment, options);
        } else {
            throw new IllegalArgumentException("Object type not supported for insertion: " + obj.getClass().getName());
        }
    }

    private void insertMainComment(MainComment mainComment) {
        Document document = new Document();
        document.append("commentId", mainComment.getCommentId())
                .append("comment", mainComment.getComment())
                .append("author", mainComment.getAuthor())
                .append("likeCount", mainComment.getLikeCount())
                .append("isReply", mainComment.isReply());

        collection.insertOne(document);
    }

    private void insertReplyComment(ReplyComment replyComment) {
        Document document = new Document();
        document.append("commentId", replyComment.getCommentId())
                .append("comment", replyComment.getComment())
                .append("author", replyComment.getAuthor())
                .append("likeCount", replyComment.getLikeCount())
                .append("isReply", replyComment.isReply())
                .append("parentMainCommentId", replyComment.getParentMainCommentId());

        collection.insertOne(document);
    }

    private void insertMainComment(MainComment mainComment, InsertOneOptions options) {
        Document document = new Document();
        document.append("commentId", mainComment.getCommentId())
                .append("comment", mainComment.getComment())
                .append("author", mainComment.getAuthor())
                .append("likeCount", mainComment.getLikeCount())
                .append("isReply", mainComment.isReply());

        collection.insertOne(document, options);
    }

    private void insertReplyComment(ReplyComment replyComment, InsertOneOptions options) {
        Document document = new Document();
        document.append("commentId", replyComment.getCommentId())
                .append("comment", replyComment.getComment())
                .append("author", replyComment.getAuthor())
                .append("likeCount", replyComment.getLikeCount())
                .append("isReply", replyComment.isReply())
                .append("parentMainCommentId", replyComment.getParentMainCommentId());

        collection.insertOne(document, options);
    }
}
