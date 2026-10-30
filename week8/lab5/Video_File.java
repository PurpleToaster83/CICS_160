public class Video_File extends Media_File {
    private int resolution;

    public Video_File(String title, double fileSize, int resolution) {
        this.resolution = resolution;
        super(title, fileSize);
    }

    public int getResolution() {
        return this.resolution;
    }

    public void play() {
       System.out.println("Playing " + "'" + title + "'" + " Video File");
    }
}
