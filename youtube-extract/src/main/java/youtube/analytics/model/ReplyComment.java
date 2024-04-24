package youtube.analytics.model;

public class ReplyComment extends MainComment {
    private String parentMainCommentId;

    public String getParentMainCommentId() {
        return parentMainCommentId;
    }

    public void setParentMainCommentId(String parentMainCommentId) {
        this.parentMainCommentId = parentMainCommentId;
    }

    @Override
    public String toString() {
        return "ReplyComment{" +
                "parentMainCommentId='" + parentMainCommentId + '\'' +
                ", commentId='" + getCommentId() + '\'' +
                ", comment='" + getComment() + '\'' +
                ", author='" + getAuthor() + '\'' +
                ", likeCount=" + getLikeCount() +
                ", isReply=" + isReply() +
                '}';
    }
}
