public class Video_File extends Media_File {
    private int resolution;

    public Video_File(String title, double file_size, int resolution) {
        this.resolution = resolution;
        super(title, file_size);
    }

    public int getResolution() {
        return this.resolution;
    }
}
