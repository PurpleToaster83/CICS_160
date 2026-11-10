import java.util.ArrayList;

public class GameStack {
    private ArrayList<GameState> history;

    public GameStack() {
        history = new ArrayList<GameState>();
    }

    public void push(GameState t) {
        this.history.add(t);
    }

    public GameState pop() {
        if(history.isEmpty()) return null;
        return this.history.remove(history.size() - 1);
    }

    public GameState peek() {
        return this.history.get(history.size() - 1);
    }

    public boolean isEmpty() {
        return (this.history.isEmpty());
    }
}
