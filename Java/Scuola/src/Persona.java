public class Persona {

    // Variables Assignament
    private String name;
    private String surname;
    private String matricola;

    // Constructor
    public Persona(String nameString, String surnameString, String matricolaString) {
        this.name = nameString;
        this.surname = surnameString;
        this.matricola = matricolaString;
    }

    // Getters
    public String getName() {
        return this.name;
    }

    public String getSurname() {
        return this.surname;
    }

    public String getMatricola() {
        return this.matricola;
    }

    // Setters
    public void setName(String nameString) {
        this.name = nameString;
    }

    public void setSurname(String surnameString) {
        this.surname = surnameString;
    }

    public void setMatricola(String matricolaString) {
        this.matricola = matricolaString;
    }
}