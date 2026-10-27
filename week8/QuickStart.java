package week8;

public class QuickStart {
    public static void main(String[] args) {
        Person p1; // variable created -- nothing contructed in heap yet (points to null)
        p1 = new Person(); // creates a person object, stored it on the heap, and returns the location to p1
        System.out.println(p1);

        Person p2 = new Person("Cole", -20, "today"); // knows what contructor to use based on parameter count + types
        System.out.println(p2);
    }
}
