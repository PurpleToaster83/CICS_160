import java.util.Scanner;

public class Wizard extends CombatEntity implements PlayerControlled {
    public Wizard(String name) {
        super(name, 100, 15);
    }

    public String attack(CombatEntity target) {
        return target.takeHit(basePower, name);
    }

    public String chooseAction(Scanner input, CombatEntity target) {
        int choice = -1;
        while (choice < 0 || choice > 3) {
            System.out.println("0. Retreat\t1. Simple Attack\t 2. Heal (Spell)\t 3. Undo (Spell)");
            if(input.hasNextInt()) {
                choice = input.nextInt();
            }
            else {
                input.next();
            }
        }

        if(choice == 0) {
            return "RETREAT";
        }
        else if(choice == 1) {
            return attack(target);
        }
        else if(choice == 2) {
            return recover(20, "Spell");
        }
        else {
            return "UNDO";
        }
    }

}
