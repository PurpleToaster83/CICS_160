import java.util.List;

public class Sorters {
    public static void selectionSort(List<Integer> lis) {
        int cur_min;
        int temp;

        for(int i = 0; i < lis.size(); i++) {
            // my_min logic
            cur_min = i;
            for(int j = i + 1; j < lis.size(); j++) {
                if(lis.get(j) < lis.get(cur_min)) {
                    cur_min = j;
                }
            }
            // swapping logic
            temp = lis.get(i);
            lis.set(i, lis.get(cur_min));
            lis.set(cur_min, temp);
        }
    }

    public static void insertionSort(List<Integer> lis) {
        int unsorted_value, sorted_index;
        boolean spot_found = false;
        for(int unsorted_index = 1; unsorted_index < lis.size(); unsorted_index++) {
            unsorted_value = lis.get(unsorted_index);
            sorted_index = unsorted_index - 1;
            while(sorted_index > 0 && !spot_found) {
                if(unsorted_value < lis.get(sorted_index)) {
                    lis.set(sorted_index + 1, lis.get(sorted_index));
                    sorted_index--;
                }
                else {
                    spot_found = true;
                }
            }
            lis.set(sorted_index + 1, unsorted_value);
        }
    }
}