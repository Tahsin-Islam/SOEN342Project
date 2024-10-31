package Model;

import java.util.Arrays;

public class Instructor {
    private String name;
    private String phoneNumber;
    private String[] specialization;
    private String startDate;
    private String endDate;

    public Instructor(String name, String phoneNumber, String[] specialization, String startDate, String endDate){
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.specialization = specialization;
        this.startDate = startDate;
        this.endDate = endDate;
    }

    public String getName() {
        return name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public String[] getSpecialization() {
        return specialization;
    }

    public String getStartDate() {
        return startDate;
    }

    public String getEndDate() {
        return endDate;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public void setSpecialization(String[] specialization) {
        this.specialization = specialization;
    }

    public void setStartDate(String startDate) {
        this.startDate = startDate;
    }

    public void setEndDate(String endDate) {
        this.endDate = endDate;
    }

    public boolean equals(Instructor anotherInstructor){
        return this.name.equals(anotherInstructor.name) && this.phoneNumber.equals(anotherInstructor.phoneNumber) &&
                Arrays.equals(this.specialization, anotherInstructor.specialization) &&
                this.startDate.equals(anotherInstructor.startDate) && this.endDate.equals(anotherInstructor.endDate);
    }
}

