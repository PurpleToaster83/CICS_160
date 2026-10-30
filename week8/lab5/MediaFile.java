public abstract class MediaFile {
    protected String title;
    private double fileSize;

    MediaFile(String title, double fileSize) {
        this.title = title;
        this.fileSize = fileSize;
    }

    abstract void play();
}
