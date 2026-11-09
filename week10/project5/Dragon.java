public class Dragon extends CombatEntity implements AIControlled {
    public Dragon(String name) {
        super(name, 150, 20);
    }

    public String attack(CombatEntity target) {
        return target.takeHit(basePower, name);
    }

    public String takeTurn(CombatEntity target) {
        int rand = (int)(Math.random() * 20) + 1;
        int healAmount = 20;
        if(rand < 16) {
            return attack(target);
        }
        else if(rand < 20) {
            target.takeHit(basePower * 3, name);
            return (name + " scorched " + target.getName()
                    + " with searing fire, dealing " +
                    (3 * basePower) + " damage");
        }
        else {
            target.takeHit(basePower * 3, name);
            recover(healAmount, "Bite");
            return (name + " took a bite out of " + target.getName()
                    + ", dealing " + (3 * basePower) +
                    " damage and recovering " + healAmount + " health!");
        }
    }
}
