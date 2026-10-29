import java.util.Arrays;

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
            data = new int[data.length * 2];

            //TODO: need to put the original data at begining of new data array
        }

        // add the item
        data[size] = newItem;
        size++;
    }

    public int pop() {
        // remove the item
        int val = data[size - 1];
        data[size - 1] = 0;
        size--;
        
        // decrease the array size based on size
        if(size < data.length / 4) {
            data = new int[Math.max(CAPACITY, data.length / 2)];
        }

        return val;
    }

    public String toString() {
        String str = "{";

        for(int i = 0; i < size; i++) {
            str += " " + data[i];
            if(i < size - 1) {
                str += ",";
            }
        }
        return str += "}";
    }

    public boolean equals(Object other) {
        if(this == other) {
            return true;
        }

        if(!(other instanceof Bag)) {
            return false;
        }
        
        int[] dataCopy = data.clone();
        Bag otherBag = (Bag) other;
        Arrays.sort(dataCopy);
        Arrays.sort(otherBag.getData());

        return Arrays.equals(data, otherBag.getData());
    }
}


