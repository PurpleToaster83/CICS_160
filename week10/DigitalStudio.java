public class DigitalStudio { // this shows the D Principle
    private DrawingTablet tablet;

    public DigitalStudio(DrawingTablet tablet) {
        this.tablet = tablet;
    }

    public void startDrawing() {
        tablet.readStylusInput();
    }

}

interface DrawingTablet {
    void readStylusInput();
}
