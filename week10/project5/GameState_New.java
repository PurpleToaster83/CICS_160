import java.util.ArrayList;

public class GameState_New {
    protected ArrayList<CombatEntity> beings;
    protected int[] beingsHealth;

    public GameState_New(ArrayList<CombatEntity> b, int[] bHealth) {
        this.beings = b;
        this.beingsHealth = bHealth;
    }

    public CombatEntity getCE(int index) {
        return this.beings.get(index);
    }

    public int getCEHealth(int index) {
        return this.beingsHealth[index];
    }

    public int getNumBeings() {
        return this.beings.size();
    }
}
