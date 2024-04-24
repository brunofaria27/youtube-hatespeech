package youtube.analytics.model;

public class ReplyComment extends MainComment {
    private String parentMainCommentId;

    public String getParentMainCommentId() {
        return parentMainCommentId;
    }

    public void setParentMainCommentId(String parentMainCommentId) {
        this.parentMainCommentId = parentMainCommentId;
    }
}
