public class AudioFile extends MediaFile {
    private double sampleRate;

    public AudioFile(String title, double fileSize, double sampleRate) {
        this.sampleRate = sampleRate;
        super(title, fileSize);
    }

    public void play() {
       System.out.println("Playing " + "'" + title + "'" + " Audio File at sample rate " + this.sampleRate);
    }
}