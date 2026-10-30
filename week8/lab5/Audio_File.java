public class Audio_File extends Media_File {
    double sampleRate;

    public Audio_File(String title, double fileSize, double sampleRate) {
        this.sampleRate = sampleRate;
        super(title, fileSize);
    }
}