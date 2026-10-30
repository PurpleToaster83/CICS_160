public class VideoFile extends MediaFile {
    private int resolution;

    public VideoFile(String title, double fileSize, int resolution) {
        this.resolution = resolution;
        super(title, fileSize);
    }

    public void play() {
       System.out.println("Playing " + "'" + this.title + "'" + " Video File at quality " + this.resolution);
    }
}
