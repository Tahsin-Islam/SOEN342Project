package Model;

public class Offering {
    private boolean isFull;
    private boolean isGroupOffering;
    private LessonType lessonType;

    public Offering(boolean isFull, boolean isGroupOffering, LessonType lessonType){
        this.isFull = isFull;
        this.isGroupOffering = isGroupOffering;
        this.lessonType = lessonType;
    }

    public boolean isFull() {
        return isFull;
    }

    public boolean isGroupOffering() {
        return isGroupOffering;
    }

    public LessonType getLessonType() {
        return lessonType;
    }

    public void setFull(boolean full) {
        isFull = full;
    }

    public void setGroupOffering(boolean groupOffering) {
        isGroupOffering = groupOffering;
    }

    public void setLessonType(LessonType lessonType) {
        this.lessonType = lessonType;
    }

    public boolean equals(Offering anotherOffering){
        return this.isFull == anotherOffering.isFull && this.isGroupOffering == anotherOffering.isGroupOffering &&
                this.lessonType == anotherOffering.lessonType;
    }
}
