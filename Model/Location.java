package Model;

public class Location {
    private String name;
    private String address;
    private String city;
    private SpaceType spaceType;
    private int capacity;

    public Location(String name, String address, String city, SpaceType spaceType, int capacity){
        this.name = name;
        this.address = address;
        this.city = city;
        this.spaceType = spaceType;
        this.capacity = capacity;
    }

    public String getName() {
        return name;
    }

    public String getAddress() {
        return address;
    }

    public String getCity() {
        return city;
    }

    public SpaceType getSpaceType() {
        return spaceType;
    }

    public int getCapacity() {
        return capacity;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public void setSpaceType(SpaceType spaceType) {
        this.spaceType = spaceType;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public boolean equals(Location anotherLocation) {
        return this.name.equals(anotherLocation.name) && this.address.equals(anotherLocation.address) &&
                this.city.equals(anotherLocation.city)  && this.spaceType.equals(anotherLocation.spaceType) &&
                this.capacity == anotherLocation.capacity;
    }
}

