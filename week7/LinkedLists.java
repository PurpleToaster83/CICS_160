import java.util.LinkedList;

class LinkedLists {
    public static void main(String[] args) {
        LinkedList<String> groceryList = new LinkedList<String>();
        groceryList.add("apples");
        groceryList.add(0, "Oil");
        groceryList.add("milk");
        groceryList.add("bread");

        System.out.println("The list has " + groceryList.size() + " elements.");
        System.out.println(groceryList);
        System.out.println(groceryList.get(0)); // indexing a specific element

        groceryList.set(0, "oil");

        System.out.println("The list has " + groceryList.size() + " elements.");
        System.out.println(groceryList);
        System.out.println(groceryList.get(0));


        LinkedList<Integer> arr1 = new LinkedList<Integer>();
        arr1.add(1);
        arr1.add(2);
        arr1.add(3);
        arr1.remove(1); // removes element at index 0
        arr1.remove(new Integer(1)); // removes element of value 1
    }
}