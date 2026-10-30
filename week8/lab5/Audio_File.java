public class Audio_File extends Media_File {
    private double sampleRate;

    public Audio_File(String title, double fileSize, double sampleRate) {
        this.sampleRate = sampleRate;
        super(title, fileSize);
    }

    public double getSampleRate() {
        return this.sampleRate;
    }
}