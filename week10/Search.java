import java.util.List;

public class Search {
    public int linearSearch(List<Integer> lis, Integer target) {
        int j = 0;
        int loc = -1;
        boolean found = false;

        while(j < lis.size() && !found) {
            if(lis.get(j).equals(target)) {
                loc = j;
                found = true;
            }
            j++;
        }
        return loc;
    }

    public int binarySearch(List<Integer> lis, Integer target) {
        int low = 0;
        int high = lis.size() - 1;
        int mid;

        while(high >= low) {
            mid = (high + low) / 2;
            if (lis.get(mid).equals(target)) {
                return mid;
            }
            else if(lis.get(mid) > target) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return -1;
    }
}
