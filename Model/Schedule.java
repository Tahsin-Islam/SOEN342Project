package Model;

public class Schedule {
    private String startDate;
    private String endDate;

    public Schedule(String startDate, String endDate){
        this.startDate = startDate;
        this.endDate = endDate;
    }

    public String getStartDate() {
        return startDate;
    }

    public String getEndDate() {
        return endDate;
    }

    public void setStartDate(String startDate) {
        this.startDate = startDate;
    }

    public void setEndDate(String endDate) {
        this.endDate = endDate;
    }

    public boolean equals(Schedule anotherSchedule){
       return this.startDate.equals(anotherSchedule.startDate) && this.endDate.equals(anotherSchedule.endDate);
    }
}
