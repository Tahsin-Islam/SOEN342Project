package Model;

public class Administrator {
    private String username;
    private String password;

    public Administrator(String username, String password){
        this.username = username;
        this.password = password;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public boolean equals(Administrator anotherAdministrator) {
        return this.username.equals(anotherAdministrator.username) &&
                this.password.equals(anotherAdministrator.password);
    }
}
