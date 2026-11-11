import java.util.Scanner;

public class GameDriver {

    private static GameState currentState;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        GameStack stack = new GameStack();
        Wizard wizard = new Wizard("Wizard");
        Dragon dragon = new Dragon("Dragon");

        CombatEntity[] entities = new CombatEntity[] {wizard, dragon};

        System.out.println("Start Game!");
        currentState = new GameState(
            entities,
            new int[] {wizard.getHealth(), dragon.getHealth()}
        );
        stack.push(currentState);
        
        boolean sideDead = false;
        boolean retreat = false;
        String endCond = "None";
        roundLoop:
        do {
            int charNum = currentState.getNumBeings();

            // print stats of all char from previous state
            for(int i = 0; i < charNum; i++) {
                CombatEntity e = currentState.getCE(i);
                System.out.println(e.getName() + " Current Health: " + e.getHealth());
                System.out.println(e.getName() + " Max Health: " + e.getMaxHealth());
                System.out.println(e.getName() + " Base Attack: " + e.getBasePower());
            }

            CombatEntity dToAttack = null;
            CombatEntity wToAttack = null;

            // player turn
            for(CombatEntity e : entities) {
                dToAttack = null;
                // attack the first dragon and wizard in the array of characters
                for(CombatEntity p : entities) {
                    if(p instanceof AIControlled && dToAttack == null && !p.hasLost()) {
                        dToAttack = p;
                    }
                }

                if(e instanceof PlayerControlled && !e.hasLost() && dToAttack != null) {
                    PlayerControlled w = (PlayerControlled)e;
                    String action = w.chooseAction(scanner, dToAttack);
                    if(action.equals("UNDO")) {
                        GameState popped = stack.pop();
                        if(stack.isEmpty()) {
                            stack.push(popped);
                        }
                        GameState undone = stack.peek();
                        for(int k = 0; k < undone.getNumBeings(); k++) {
                            undone.getCE(k).setHealth(undone.getCEHealth(k));
                        }
                        currentState = stack.peek();
                        System.out.println(e.getName() + " casts a spell to turn back time");
                        continue roundLoop;
                    }
                    else if(action.equals("RETREAT")) {
                        System.out.println(e.getName() + " runs away, and lives to fight another day");
                        retreat = true;
                        break roundLoop;
                    }
                    System.out.println(action);
                }
            }

                for(CombatEntity p : entities) {
                    if(p instanceof PlayerControlled && wToAttack == null && !p.hasLost()) {
                        wToAttack = p;
                    }
                }

            // enemy turn
            for(CombatEntity e : entities) {
                wToAttack = null;
                if(e instanceof AIControlled && !e.hasLost()) {
                    AIControlled d = (AIControlled) e;
                    System.out.println(d.takeTurn(wToAttack));
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

        boolean wLeft = false;
        for(CombatEntity remaining : entities) {
            if(remaining instanceof PlayerControlled && !remaining.hasLost()) {
                wLeft = true;
            }
        }
        if(retreat) {
            endCond = "A Wizard Escaped";
        }
        else if(wLeft) {
            endCond = "Wizard Victory";
        }
        else {
            endCond = "The Dragons Defeated the Wizards";
        }
        System.out.println(endCond);
    }

    public static GameState getCurrentGameState() {
        return currentState;
    }
}
