public abstract class Media {
    private String title;
    private double fileSize; //MB

    public Media(String title, double fileSize) {
        //added for Activity 5
        if (title == null || title.isEmpty()) {
            this.title = "Untitled File";
        } else {
            this.title = title;
        }

        if (fileSize <= 0) {
            this.fileSize = 1.0; //Default to 1MB if corrupted
        } else {
            this.fileSize = fileSize;
        }
    }

    public abstract void play();

    public String getTitle() { return title; }
    public double getFileSize() { return fileSize; }

    @Override
    public String toString() {
        return String.format("[%s] %s (%.2f MB)", this.getClass().getSimpleName(), title, fileSize);
    }
}