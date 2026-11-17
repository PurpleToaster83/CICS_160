import java.io.File;
import java.util.ArrayList;

public class MergeSort {
    public static int searchFileSize(ArrayList<File> files, double target){
        int low = 0;
        int high = files.size()-1;
        int mid;
        while (high >= low){
            mid = (high+low)/2;
            if (files.get(mid).length() == target){
                return mid;
            }
            else if (files.get(mid).length() > target){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return -1;
    }
}
