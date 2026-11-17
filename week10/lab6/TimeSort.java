import java.io.File;
import java.util.ArrayList;
import java.util.Random;

public class TimeSort {
    private static ArrayList<Media> createRandomFiles(int count, Random random){
        ArrayList<Media> files = new ArrayList<>();
        for (int i = 0; i < count; i++){
            String title = "Test Media " + i;
            double size = random.nextInt(1000000) + 1;
            if (random.nextBoolean()){
                files.add(new Audio(title, size, "44.1kHz"));
            }
            else{
                files.add(new Video(title, size, "1080p", 128));
            }
        }
        return files;
    }


    private static void timeSort(int count, Random random){
       ArrayList<Media> files = createRandomFiles(count, random);
       long startTime = System.nanoTime();
       sortFileSize(files);
       long elapsedTime = System.nanoTime() - startTime;
       double elapsedMilliseconds = Math.round(elapsedTime / 1000.0) / 1000.0;
       System.out.println("Sorting " + count + " files took "
               + elapsedMilliseconds + " ms.");
   }


   private static void reportSortTimes(){
       int[] sizes = {10, 1000, 10000};
       Random random = new Random();
       for (int size : sizes){
           timeSort(size, random);
       }
   }

   private static void sortFileSize(ArrayList<Media> files) {
    QuickSort.sortFileSize(files);
   }


   public static void main(String[] args){
       reportSortTimes();
   }

}
