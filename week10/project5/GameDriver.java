import java.util.Scanner;
import java.util.ArrayList;

public class GameDriver {

    private static GameState currentState;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        GameStack stack = new GameStack();
        Wizard wizard = new Wizard("Wizard");
        Dragon dragon = new Dragon("Dragon");

        CombatEntity[] entities = new CombatEntity[] {wizard, dragon};

        System.out.println("Start Game!");
        GameState beginState = new GameState(
            entities,
            new int[] {wizard.getHealth(), dragon.getHealth()}
        );
        stack.push(beginState);
        
        boolean sideDead = false;
        String endCond = "None";
        roundLoop:
        do { // TODO: keep everything in one array
            ArrayList<Integer> dead = new ArrayList<Integer>();
            int charNum = currentState.getNumBeings();

            // print stats of all char from previous state
            for(int i = 0; i < charNum; i++) {
                CombatEntity e = currentState.getCE(i);
                System.out.println(e.getName() + " Current Health: " + e.getHealth());
                System.out.println(e.getName() + " Max Health: " + e.getMaxHealth());
                System.out.println(e.getName() + " Base Attack: " + e.getBasePower());

                if(e.hasLost()) {
                    dead.add(i);
                }
            }

            // attack the first dragon and wizard in the array of characters
            CombatEntity dToAttack = null;
            CombatEntity wToAttack = null;
            for(CombatEntity e : entities) {
                if (dToAttack != null && wToAttack != null) {
                    break;
                }
                if(e instanceof AIControlled && dToAttack == null && !e.hasLost()) {
                    dToAttack = e;
                }
                else if(e instanceof PlayerControlled && wToAttack == null && !e.hasLost()) {
                    wToAttack = e;
                }
            }

            // player turn
            for(CombatEntity e : entities) {
                if(e instanceof PlayerControlled) {
                    Wizard w = (Wizard)e;
                    String action = w.chooseAction(scanner, dToAttack);
                    System.out.println(action);
                    if(action.equals("UNDO")) {
                        stack.pop();
                        GameState undone = stack.peek();
                        for(int k = 0; k < undone.getNumBeings(); k++) {
                            undone.getCE(k).setHealth(undone.getCEHealth(k));
                        }
                        System.out.println(w.getName() + " casts a spell to turn back time");
                        continue roundLoop;
                    }
                    else if(action.equals("RETREAT")) {
                        System.out.println(w.getName() + " runs away and lives to fight another day");
                        endCond = "A Wizard Retreated";
                        break roundLoop;
                    }
                }
            }

            // enemy turn
            for(CombatEntity e : entities) {
                if(e instanceof AIControlled && !e.hasLost()) {
                    System.out.println(e.attack(wToAttack));
                }
            }

            boolean d = false;
            boolean w = false;
            for(CombatEntity e : entities) {
                if(e instanceof PlayerControlled && !e.hasLost()) {
                    w = true;
                }
                else if(e instanceof AIControlled && !e.hasLost()) {
                    d = true;
                }
            }

            int[] newHealths = new int[entities.length];
            for(int h = 0; h < entities.length; h++) {
                newHealths[h] = currentState.getCE(h).getHealth();
            }
            sideDead = !(d && w);
            currentState = new GameState(entities, newHealths);
            stack.push(currentState);

        }
        while (!sideDead);

        boolean dLeft = false;
        for(CombatEntity remaining : entities) {
            if(remaining instanceof AIControlled) {
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
