public class GameState {
    protected CombatEntity[] beings;
    protected int[] beingsHealth;

    public GameState(CombatEntity[] b, int[] bHealth) {
        this.beings = b;
        this.beingsHealth = bHealth;
    }

    public CombatEntity getCE(int index) {
        return this.beings[index];
    }

    public int getCEHealth(int index) {
        return this.beingsHealth[index];
    }

    public int getNumBeings() {
        return this.beings.length;
    }
}
