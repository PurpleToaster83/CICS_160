public class VideoFile extends MediaFile {
    private int resolution;

    public VideoFile(String title, double fileSize, int resolution) {
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
