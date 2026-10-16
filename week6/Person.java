package week6;

public class Person {
    private String name;
    private  String adress;
    private String phone;

    Person(String newName, String address, String phone) {
        this.name = newName;
        this.adress = address;
        this.phone = phone;
    }

    public String getName() {
        return this.name;
    }
}
