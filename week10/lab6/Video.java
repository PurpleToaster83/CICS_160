// Video: Implements Streamable
public class Video extends Media implements Streamable {
    private String resolution;
    private int bitrate;

    public Video(String title, double fileSize, String resolution, int bitrate) {
        super(title, fileSize);
        this.resolution = resolution;
        this.bitrate = bitrate;
    }

    @Override
    public void play() {
        System.out.println("Rendering frames at " + resolution);
    }

    @Override
    public void buffer() {
        System.out.println("Buffering video: " + getTitle() + "...");
    }

    @Override
    public int getBitrate() { return bitrate; }
}
