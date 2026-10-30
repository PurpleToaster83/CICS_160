public class Video_File extends Media_File {
    int resolution;

    public Video_File(String title, double file_size, int resolution) {
        this.resolution = resolution;
        super(title, file_size);
    }
}
