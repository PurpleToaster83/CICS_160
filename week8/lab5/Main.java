import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int n = 5;
        Random rand = new Random();
        ArrayList<MediaFile> files = new ArrayList<MediaFile>();

        for(int i = 1; i < n; i++) {
            files.add(new VideoFile("Video" + i, i * rand.nextDouble(100), rand.nextInt(1000)));
            files.add(new AudioFile("Audio" + i, i * rand.nextDouble(100), rand.nextDouble(500)));
        }

        Main.playAll(files);
    }

    public static void playAll(ArrayList<MediaFile> files) {
        for(MediaFile file : files) {
            file.play();
        }
    }
}
