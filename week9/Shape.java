package week9;

public abstract class Shape {
    protected Point position;
    abstract double computeArea();

    public Point getPosition() {
        return this.position;
    }

    public void setPosition(Point position) {
        this.position = position;
    }

    public void movePositionRelative(Point p) {
        double x = this.position.getX() + p.getX();
        double y = this.position.getY() + p.getY();
        this.position.setX(x);
        this.position.setY(y);
    }
}
