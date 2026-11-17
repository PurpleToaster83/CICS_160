public class Goblin extends CombatEntity implements AIControlled {
    private double pSwarm;

    public Goblin(String name, double pSwarm) {
        super(name, 75, 5);
        this.pSwarm = pSwarm;
    }

    public String attack(CombatEntity target) {
        return target.takeHit(basePower, name);
    }

    public String takeTurn(CombatEntity target) {
        if (Math.random() >= pSwarm) {
            return attack(target);
        }

        int rand = (int)(Math.random() * 5) + 1;
        int landed = 0;


        for(int g = 0; g <= rand && !target.hasLost(); g++) {
           attack(target);
           landed++;
        }

        String msg = getName() + " calls " + rand + " goblins to the swarm";
        if(target.hasLost()) {
            return msg + ", killing " + target.getName();
        }
        return msg + ", dealing a total of " + (landed * basePower) + " damage";
    }
}
