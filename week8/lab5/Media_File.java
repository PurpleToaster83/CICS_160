public abstract class Media_File {
    protected String title;
    private double fileSize;

    Media_File(String title, double fileSize) {
        this.title = title;
        this.fileSize = fileSize;
    }

    abstract void play();
}
