package week8;

public class Person {
    private String name;
    private int age;
    private String birthDate;

    Person() {
        this.name = "";
        this.age = -1;
        this.birthDate = "1/1/1970";
    }

    Person(String n, int a, String bd) {
        this.name = n;
        this.age = a;
        this.birthDate = bd;
    }

    Person(String n) {
        this.name = n;
        this.age = -1;
        this.birthDate = "1/1/1970";  
    }
}
