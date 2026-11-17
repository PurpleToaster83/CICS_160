//Audio: Not Streamable
public class Audio extends Media {
    private String sampleRate;

    public Audio(String title, double fileSize, String sampleRate) {
        super(title, fileSize);
        this.sampleRate = sampleRate;
    }

    @Override
    public void play() {
        System.out.println("Outputting sound at " + sampleRate);
    }
}