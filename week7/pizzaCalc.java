public class pizzaCalc {
    static double pi = 3.1459;
    public double radius;
    int diameter;
    String[] toppings;
    
    pizzaCalc(int d, String[] toppin) {
        this.diameter = d;
        this.radius = diameter / 2.0;
        this.toppings = toppin;
    }

    pizzaCalc(int d) {
        this.diameter = d;
        this.radius = diameter / 2.0;
        this.toppings = null;
    }

    public double my_area() {
        return pi * this.radius * this.radius;
    }

    public static double circle_area(double r) { // does not require a specific class
        return pi * r * r; // not use object specific info
    }
}
