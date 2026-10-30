package week8.lab5;

public abstract class Media_File {
    protected String title;
    protected double file_size;

    Media_File(String title, double file_size) {
        this.title = title;
        this.file_size = file_size;
    }
}
