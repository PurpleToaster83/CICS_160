package week8;

public class Student extends Person{
    private String Major;

    public Student(String N, int A, String BD, String M) {
        super(N, A, BD);
        this.Major = M;
    }

    public Student(String M) {
        super();
        this.Major = M;
    }

    public String getMajor() {
        return this.Major;
    }

    public boolean canVote() {
        return this.age >= 18;
    }
    
    @Override // tag to say how function works
    public String toString() {
        return super.toString() + ". My Major is " + this.getMajor();
    }
}
