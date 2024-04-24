package youtube.analytics.model;

public class MainComment {
    private String commentId;
    private String comment;
    private String author;
    private long likeCount;
    private boolean isReply;

    public String getCommentId() {
        return commentId;
    }

    public void setCommentId(String commentId) {
        this.commentId = commentId;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    
    public long getLikeCount() {
        return likeCount;
    }

    public void setLikeCount(Long long1) {
        this.likeCount = long1;
    }

    public boolean isReply() {
        return isReply;
    }

    public void setReply(boolean isReply) {
        this.isReply = isReply;
    }

    @Override
    public String toString() {
        return "MainComment{" +
                "commentId='" + commentId + '\'' +
                ", comment='" + comment + '\'' +
                ", author='" + author + '\'' +
                ", likeCount=" + likeCount +
                ", isReply=" + isReply +
                '}';
    }
}
