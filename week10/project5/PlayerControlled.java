import java.util.Scanner;

public interface PlayerControlled {
    public String chooseAction(Scanner input, CombatEntity target);
}
