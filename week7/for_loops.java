public class for_loops {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};

        // for each loop
        for(int elem : arr) { // can use more generic term for class here (like parent classes)
            System.out.println(elem);
        }

        int i = 0;
        // do-while loop
        do {
            System.out.println(i);
            i++;
        } while (i < 10);
    }

}
