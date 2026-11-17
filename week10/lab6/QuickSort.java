import java.util.ArrayList;

public class QuickSort {
    public static void sortFileSize(ArrayList<Media> files){
        for (int i = 0; i < files.size() - 1; i++){
            int smallestIndex = i;
            for (int j = i + 1; j < files.size(); j++){
                if (files.get(j).getFileSize() < files.get(smallestIndex).getFileSize()){
                    smallestIndex = j;
                }
            }
            if (smallestIndex != i){
                Media temp = files.get(i);
                files.set(i, files.get(smallestIndex));
                files.set(smallestIndex, temp);
            }
        }
    }
}
