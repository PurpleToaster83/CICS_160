import java.util.ArrayList;;

public class Using_Arraylists {
    public static void main(String[] args) {
        ArrayList<String> groceryList = new ArrayList<String>();
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
    }
}
