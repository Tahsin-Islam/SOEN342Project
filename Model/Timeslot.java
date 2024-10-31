package Model;

public class Timeslot {
    private String startTime;
    private String endTime;

    public Timeslot(String startTime, String endTime){
        this.startTime = startTime;
        this.endTime = endTime;
    }

    public String getStartTime() {
        return startTime;
    }

    public String getEndTime() {
        return endTime;
    }

    public void setStartTime(String startTime) {
        this.startTime = startTime;
    }

    public void setEndTime(String endTime) {
        this.endTime = endTime;
    }

    public boolean equals(Timeslot anotherTimeslot){
        return this.startTime.equals(anotherTimeslot.startTime) &&
                this.endTime.equals(anotherTimeslot.endTime);
    }
}
