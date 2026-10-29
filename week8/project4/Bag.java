public class Bag {
    private int[] data;
    private int size;
    private static final int CAPACITY = 10;

    Bag() {
        data = new int[CAPACITY];
        size = 0;
    }

    public int[] getData() {
        return data;
    }

    public void add(int newItem) {
        // increase the array size if neccesary
        if(size >= data.length) {
            int [] newLength = new int[data.length * 2];
            for(int i = 0; i < size; i++) {
                newLength[i] = data[i];
            }
            data = newLength;
        }

        // add the item
        data[size] = newItem;
        size++;
    }

    public int pop() {
        // throw error if empty
        if(size == 0) {
            throw new  java.util.NoSuchElementException("Bag is empty");
        }

        // store the value at the end, and set element to zero
        int val = data[size - 1];
        data[size - 1] = 0;
        size--;
        
        // decrease the array size based on size
        if(size < data.length / 4) {
            System.out.println("here");
            int [] newLength = new int[Math.max(CAPACITY, data.length / 2)];
            for(int i = 0; i < size; i++) {
                newLength[i] = data[i];
            }
            data = newLength;
        }

        return val;
    }

    public String toString() {
        String str = "{";

        // add element and comma for each item
        for(int i = 0; i < size; i++) {
            str += " " + data[i];

            // don't have comma at end
            if(i < size - 1) {
                str += ",";
            }
        }
        return str += "}";
    }

    private void sort() {
        if (data == null || data.length <= 1) {
            return;
        }
        dualPivotQuicksort(0, size - 1); // avg: O(nlogn), worst: O(n^2)
    }

    private void dualPivotQuicksort(int low, int high) {
        // base case
        if(low >= high) {
            return;
        }

        if(data[low] > data[high]) {
            // swap element positions
            int temp = data[low];
            data[low] = data[high];
            data[high] = temp;
        }

        // two pivots
        int p1 = data[low];
        int p2 = data[high];

        int lt = low + 1;
        int gt = high - 1;
        int i = low + 1;

        while(i <= gt) {
            if(data[i] < p1) {
                // swap element positions
                int temp = data[i];
                data[i] = data[lt];
                data[lt] = temp;
                lt++;
                i++;
            }
            else if(data[i] > p2) {
                // swap element positions
                int temp = data[i];
                data[i] = data[gt];
                data[gt] = temp;
                gt--;
            }
            else {
                i++;
            }
        }

        lt--;
        gt++;
        // swap low and lt and also high and gt elements
        int temp = data[low];
        data[low] = data[lt];
        data[lt] = temp;
        temp = data[high];
        data[high] = data[gt];
        data[gt] = temp; 

        // sort the three sub-arrays
        dualPivotQuicksort(low, lt - 1);
        dualPivotQuicksort(gt + 1, high);
        if(p1 < p2) {
            dualPivotQuicksort(lt + 1, gt - 1);
        }
    }

    public boolean equals(Object other) {
        // check if other is the exact same
        if(this == other) {
            return true;
        }

        // check if other is type Bag
        if(!(other instanceof Bag)) {
            return false;
        }
        
        // cast other into type bag, get data, and check size
        Bag otherBag = (Bag) other;
        int[] otherData = otherBag.getData();
        if(size != otherBag.size) {
            return false;
        }

        // sort both in-place using Dual Pivot Sort
        this.sort();
        otherBag.sort();

        // go through and check the filled in elements are the same
        for(int i = 0; i < size; i++) {
            if(data[i] != otherData[i]) {
                return false;
            }
        }
        
        return true;
    }
}


