package week8;

public class QuickStart {
    public static void main(String[] args) {
        Person p1; // variable created -- nothing contructed in heap yet (points to null)
        p1 = new Person(); // creates a person object, stored it on the heap, and returns the location to p1
        System.out.println(p1.toString());

        Person p2 = new Person("Cole", -20, "today"); // knows what contructor to use based on parameter count + types
        System.out.println(p2.toString());

        Student s1 = new Student("CS");
        String s1_as_st = s1.toString(); // references most direct linked toString (student's one)
        // if want to use person to string need to reference object as a person
        // resolution - checks immediate area, then checks class, then parent class, etc
        // if caste as a person it only is treat as person not convert to person

        System.out.println(get_toString(p2));
        System.out.println(get_toString(s1));
    }

    static public String get_toString(Person p) {
        return p.toString();
    }
}
