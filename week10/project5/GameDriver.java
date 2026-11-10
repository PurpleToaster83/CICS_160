import java.util.Scanner;
import java.util.ArrayList;;

public class GameDriver {

    private static GameState currentState;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        GameStack stack = new GameStack();
        Wizard wizard = new Wizard("Wizard");
        Dragon dragon = new Dragon("Dragon");

        System.out.println("Start Game!");
        GameState beginState = new GameState(
            new CombatEntity[] {wizard, dragon},
            new int[] {wizard.getHealth(), dragon.getHealth()}
        );
        stack.push(beginState);
        
        boolean cont = false;
        String endCond = "None";
        do {
            ArrayList<Integer> dead = new ArrayList<Integer>();
            int charNum = stack.peek().getNumBeings();

            // print stats of all char from previous state
            for(int i = 0; i < charNum; i++) {
                CombatEntity e = stack.peek().getCE(i);
                System.out.println(e.getName() + " Current Health: " + e.getHealth());
                System.out.println(e.getName() + " Max Health: " + e.getMaxHealth());
                System.out.println(e.getName() + " Base Attack: " + e.getBasePower());

                if(e.hasLost()) {
                    dead.add(i);
                }
            }
            cont = !dead.isEmpty();

            // attack the first dragon and wizard in the array of characters
            Dragon dToAttack = null;
            Wizard wToAttack = null;
            for(CombatEntity e : stack.peek().getBeings()) {
                if (dToAttack != null && dToAttack != null) {
                    break;
                }
                if(e instanceof Dragon && dToAttack == null) {
                    dToAttack = (Dragon)e;
                }
                else if(e instanceof Wizard && wToAttack == null) {
                    wToAttack = (Wizard)e;
                }
            }

            // player turn
            for(CombatEntity e : stack.peek().getBeings()) {
                if(e instanceof Wizard) {
                    Wizard w = (Wizard)e;
                    String action = w.chooseAction(scanner, dToAttack);
                    System.out.println(action);
                    if(action.equals("UNDO")) {
                        stack.pop();
                        System.out.println(w.getName() + " casts a spell to turn back time");
                    }
                    else if(action.equals("RETREAT")) {
                        cont = false;
                        System.out.println(w.getName() + " runs away and lives to fight another day");
                        endCond = "A Wizard Retreated";
                    }
                }
            }
            if(cont == false) {
                break;
            }

            // enemy turn
            for(CombatEntity e : stack.peek().getBeings()) {
                if(e instanceof Dragon) {
                    Dragon d = (Dragon)e;
                    System.out.println(d.attack(wToAttack));
                }
            }

            // determine who is dead/alive and make new state
            CombatEntity[] aliveChar = new CombatEntity[charNum - dead.size()];
            int[] aliveHealth = new int[charNum - dead.size()];
            int skip = 0;
            for(int i = 0; i < charNum; i++) {
                if(dead.indexOf(i) == -1) {
                    aliveChar[i - skip] = stack.peek().getCE(i);
                    aliveHealth[i - skip] = stack.peek().getCE(i).getHealth();
                }
                else {
                    skip++;
                }
            }
            stack.push(new GameState(aliveChar, aliveHealth));

        }
        while (cont);

        boolean dLeft = false;
        for(CombatEntity remaining : stack.peek().getBeings()) {
            if(remaining instanceof Dragon) {
                dLeft = true;
            }
        }
        if(dLeft) {
            if(!endCond.equals("None")) {
                endCond = "The Dragons Defeated the Wizards";
            }
        }
        else {
            endCond = "The Wizards Won!";
        }
        System.out.println(endCond);
    }

    public static GameState getCurrentGameState() {
        return currentState;
    }
}
