package week9;

import java.util.ArrayList;
import java.util.LinkedList;

public class Quickstart {
    public static ArrayList<Integer> collatzConjecture(int i) {
        ArrayList<Integer> steps = new ArrayList<>();

        while(i != 1) {
            if (i % 2 == 0) {
                i /= 2;
            }
            else {
                i *= 3;
                i++;
            }
            steps.add(i);
        }
        steps.add(i);
        return steps;
    }

    public static void filter(int[] lis) {
        // ArrayList<Integer> return_list = new ArrayList<>();
        LinkedList<Integer> return_list = new LinkedList<>();

        for(int i = 0; i < lis.length; i++) {
            if (i % 2 == 0) {
                return_list.add(lis[i] + 3);
            }
        }
    }
    
    public static void main(String[] args) {

    }
}
