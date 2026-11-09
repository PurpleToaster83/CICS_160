public abstract class CombatEntity {
    protected String name;
    protected int curHealth;
    protected int maxHealth;
    protected int basePower;

    public CombatEntity(String n, int h, int p) {
        this.name = n;
        this.maxHealth = h;
        this.basePower = p;

        this.curHealth = this.maxHealth;
    }

    public boolean hasLost() {
        return (this.curHealth <= 0);
    }

    public String takeHit(int damage, String source) {
        this.curHealth -= damage;
        return this.name + " takes a hit for " + damage + " damage from " + source;
    }

    public String recover(int amount, String source) {
        if(this.curHealth + amount >= 100) {
            amount = 100 - this.curHealth;
        }
        return this.name + " recovers " + amount + " health from  " + source;
    }

    public String getName() {
        return this.name;
    }

    public void setHealth(int health) {
        this.curHealth = health;
    }

    public int getHealth() {
        return this.curHealth;
    }

    public int getMaxHealth() {
        return this.maxHealth;
    }

    public int getBasePower() {
        return this.basePower;
    }

    public abstract String attack(CombatEntity target);
}