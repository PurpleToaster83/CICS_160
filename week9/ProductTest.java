package week9;

abstract class Product {
    int multiplyBy;

    Product(int multiplyBy) {
        this.multiplyBy = multiplyBy;
    }

    public int multiply(int val) {
        return multiplyBy * val;
    }
}

class TimesTwo extends Product {
    public TimesTwo() {
        super(2);
    }
}

public class ProductTest {
    public static void main(String[] args) {
        Product p = new TimesTwo();
    }
}
