import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int n = 5;
        Random rand = new Random();
        ArrayList<Media_File> files = new ArrayList<Media_File>();

        for(int i = 1; i < n; i++) {
            files.add(new Video_File("Video" + i, i * rand.nextDouble(100), rand.nextInt(1000)));
            files.add(new Audio_File("Audio" + i, i * rand.nextDouble(100), rand.nextDouble(500)));
        }

        Main.playAll(files);
    }

    public static void playAll(ArrayList<Media_File> files) {
        for(Media_File file : files) {
            file.play();
        }
    }
}
