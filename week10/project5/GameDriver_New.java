import java.util.Scanner;
import java.util.ArrayList;

public class GameDriver_New {

    private static GameState_New currentState;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        GameStack_New stack = new GameStack_New();
        Wizard wizard = new Wizard("Wizard");
        Dragon dragon = new Dragon("Dragon");
        Goblin goblin = new Goblin("Goblin", 0.5);


        // CombatEntity[] entities = new CombatEntity[] {wizard, dragon};
        ArrayList<CombatEntity> entities = new ArrayList<CombatEntity>();
        entities.add(wizard);
        entities.add(dragon);
        entities.add(goblin);

        int[] startHealth = new int[entities.size()];
        for(int h = 0; h < entities.size(); h++) {
            startHealth[h] = entities.get(h).getHealth();
        }

        System.out.println("Start Game!");
        currentState = new GameState_New(entities, startHealth);
        stack.push(currentState);
        
        boolean sideDead = false;
        String retreat = null;
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
                        GameState_New popped = stack.pop();
                        if(stack.isEmpty()) {
                            stack.push(popped);
                        }
                        GameState_New undone = stack.peek();
                        for(int k = 0; k < undone.getNumBeings(); k++) {
                            undone.getCE(k).setHealth(undone.getCEHealth(k));
                        }
                        currentState = stack.peek();
                        System.out.println(e.getName() + " casts a spell to turn back time");
                        continue roundLoop;
                    }
                    else if(action.equals("RETREAT")) {
                        System.out.println(e.getName() + " runs away, and lives to fight another day");
                        retreat = e.getName();
                        break roundLoop;
                    }
                    System.out.println(action);
                }
            }

            // enemy turn
            for(CombatEntity e : entities) {
                wToAttack = null;

                for(CombatEntity p : entities) {
                    if(p instanceof PlayerControlled && wToAttack == null && !p.hasLost()) {
                        wToAttack = p;
                    }
                }

                if(e instanceof AIControlled && !e.hasLost()) {
                    AIControlled d = (AIControlled) e;
                    if(wToAttack != null) {
                        System.out.println(d.takeTurn(wToAttack));
                    }
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

            int[] newHealths = new int[entities.size()];
            for(int h = 0; h < entities.size(); h++) {
                newHealths[h] = entities.get(h).getHealth();
            }
            sideDead = !(d && w);
            currentState = new GameState_New(entities, newHealths);
            stack.push(currentState);

        }
        while (!sideDead);

        boolean wLeft = false;
        for(CombatEntity remaining : entities) {
            if(remaining instanceof PlayerControlled && !remaining.hasLost()) {
                wLeft = true;
            }
        }
        if(retreat != null) {
            endCond = retreat + " Escaped";
        }
        else if(wLeft) {
            endCond = "Wizard Victory";
        }
        else {
            endCond = "The Wizards have been Defeated";
        }
        System.out.println(endCond);
    }

    public static GameState_New getCurrentGameState() {
        return currentState;
    }
}
