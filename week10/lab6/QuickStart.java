import java.util.ArrayList;

public class QuickStart {
    public static void main(String[] args) {
        ArrayList<Media> media = new ArrayList<Media>();

        for(int i = 0; i <= 10; i++) {
            if(i % 2 == 0) {
                media.add(new Audio(
                    "File " + i, (int)(Math.random() * 1000), (int)(Math.random() * 1000) + " hz"
                ));
            }
            else {
                media.add(new Video(
                    "File " + i, (int)(Math.random() * 1000), (int)(Math.random() * 1000) + " ppm", (int)(Math.random() * 1000)
                ));
            }

        }

        QuickSort.sortFileSize(media);

        for(Media m : media) {
            System.out.println("Name: " + m.getTitle() + ", Type: " + m.getClass() + ", FileSize: " + m.getFileSize());
        }
    }
}
