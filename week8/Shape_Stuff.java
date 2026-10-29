package week8;

import java.util.ArrayList;

public class Shape_Stuff {
    public static void main(String[] args) {
        // ArrayList<Object> shapes = new ArrayList<Object>();
        // Circle c1 = new Circle(4.0);
        // Square s1 = new Square(4.0);
        // shapes.add(c1);
        // shapes.add(s1);
        // double total = 0;
        // for(Object obj : shapes) {
        //     if(obj instanceof Circle c) total += 3.14 * c.get_rad() * c.get_rad(); // not need curly braces if in one line
        //     else if (obj instanceof Square s) total += s.get_length() * s.get_length(); // converts to use the iterated variable as the type
        // }

        ArrayList<Shape> shapes = new ArrayList<Shape>();
        Circle c1 = new Circle(4.0);
        Square s1 = new Square(4.0);
        shapes.add(c1);
        shapes.add(s1);
        double total = 0;
        for(Shape s : shapes) {
            total += s.area();
        }
        System.out.println(total);
    }

}

interface Shape {
    double area();
}


// can have multiple classes in the file because they are not public
// 1 public class per file
class Circle implements Shape {
    private double rad;

    Circle(double r) {
        this.rad = r;
    }

    public double get_rad() {
        return this.rad;
    }

    public double area() {
        return 3.14 * this.rad *  this.rad;
    }
}

class Square implements Shape {
    private double length;

    Square(double l) {
        this.length = l;
    }

    public double get_length() {
        return this.length;
    }

    public double area() {
        return this.length * this.length;
    }
}
