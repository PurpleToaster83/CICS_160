public class Quickstart {
    public static void main(String[] args) {
        Bag bag = new Bag();
        for(int i = 0; i < 25; i++) {
            bag.add(i);
        }
        System.out.println(bag.toString());
    }
}