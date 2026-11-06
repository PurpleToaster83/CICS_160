package week9;

public class Rectangle extends Shape {
    protected Point position;
    protected double length;
    protected double width;

    public Rectangle(Point upperLeft, double length, double width) {
        this.position = upperLeft;
        this.length = length;
        this.width = width;
    }

    public double computeArea() {
        return this.length * this.width;
    }
}
