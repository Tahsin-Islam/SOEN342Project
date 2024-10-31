package Model;

public class Lesson {
    private LessonType lessonType;
    private boolean mode;

    public Lesson(LessonType lessonType, boolean mode){
        this.lessonType = lessonType;
        this.mode = mode;
    }

    public LessonType getLessonType() {
        return lessonType;
    }

    public void setLessonType(LessonType lessonType) {
        this.lessonType = lessonType;
    }

    public boolean isMode() {
        return mode;
    }

    public void setMode(boolean mode) {
        this.mode = mode;
    }

    public boolean equals(Lesson anotherLesson){
        return this.lessonType == anotherLesson.lessonType && this.mode == anotherLesson.mode;
    }
}
