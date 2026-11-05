package week9;

public class Course {
    private String instructor;
    private int roomNum;
    private int maxStudents;
    protected Student[] students;

    public Course() {
        this.instructor = "None";
        this.roomNum = 0;
        this.maxStudents = 50;
        this.students = new Student[1];
        this.students[0] = new Student();
    }

    public Course(int roomNum, int maxStudents, Student[] students) {
        this.instructor = "None";
        this.roomNum = roomNum;
        this.maxStudents = maxStudents;
        this.students= students;
    }

    public Course(String instructor, int roomNum, int maxStudents, Student[] students) {
        this.instructor = instructor;
        this.roomNum = roomNum;
        this.maxStudents = maxStudents;
        this.students= students;
    }

    public void addStudent(Student student) {
        Student[] new_lis = new Student[this.students.length + 1];
        for(int i = 0; i < new_lis.length; i++) {
            new_lis[i] = this.students[i];
        }
        new_lis[this.students.length] = student;
        this.students = new_lis;
    }
}

class HardCourse extends Course {
    int difficulty;

    public HardCourse(int diff) {
        this.difficulty = diff;
        super();
    }

    public void dropClass(String name) {
        int skip = 0;
        for(int j = 0; j < this.students.length; j++) {
            if(this.students[j].name.equals(name)) {
                Student[] dropped = new Student[this.students.length - 1];
                for(int k = 0; k < this.students.length; k++) {
                    if(k == j) {
                        skip = 1;
                        continue;
                    }
                    dropped[k] = this.students[k + skip];
                }
                this.students = dropped;
                break;
            }
        }
    }
}

class Student {
    public String name;
    public double grade;

    public Student() {
        this.name = "Student";
        this.grade = 0.00;
    }
}
