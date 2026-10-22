public class QuickStart {
    public static void main(String[] args) {
        pizzaCalc  pizza1 = new pizzaCalc(16);
        System.out.println(pizza1.my_area());
        System.out.println(pizza1.radius);

        double a = pizzaCalc.circle_area(8.0);
        System.out.println(pizzaCalc.pi);
    }
}
