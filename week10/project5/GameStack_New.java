import java.util.ArrayList;

public class GameStack_New {
    private ArrayList<GameState_New> history;

    public GameStack_New() {
        history = new ArrayList<GameState_New>();
    }

    public void push(GameState_New t) {
        this.history.add(t);
    }

    public GameState_New pop() {
        if(history.isEmpty()) return null;
        return this.history.remove(history.size() - 1);
    }

    public GameState_New peek() {
        return this.history.get(history.size() - 1);
    }

    public boolean isEmpty() {
        return (this.history.isEmpty());
    }
}
