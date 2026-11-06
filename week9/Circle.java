package week9;

public class Circle extends Shape {
    protected Point position;
    protected double radius;
    private double diameter;

    Circle(Point center, double radius) {
        this.position = center;
        this.radius = radius;
        this.diameter = radius * 2;
    }

    public double computeArea() {
        return 3.14 * this.radius * this.radius;
    }

    public double getDiameter() {
        return this.diameter;
    }
}
