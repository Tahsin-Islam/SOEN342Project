package Model;

public class Client {
    private String name;
    private int age;
    private String phoneNumber;

    public Client(String name, int age, String phoneNumber){
        this.name = name;
        this.age = age;
        this.phoneNumber = phoneNumber;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public boolean equals(Client anotherClient) {
        return this.name.equals(anotherClient.name) && this.age == anotherClient.age &&
                this.phoneNumber.equals(anotherClient.phoneNumber);
    }
}
