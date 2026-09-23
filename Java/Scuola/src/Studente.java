import java.util.ArrayList;
import java.util.List;

public class Studente {

    private List<Object> corsi = new ArrayList<Object>();

    // Constructor
    public Studente(List<Object> corsiList) {
        this.corsi = corsiList;
    }

    // Getters
    public List<Object> getCorsi() {
        return this.corsi;
    }

    // Setters
    public void setCorsi(List<Object> corsiList) {
        this.corsi = corsiList;
    }

    // Utility
    public void addCorso(Object corsoObject) {
        this.corsi.add(corsoObject);
    }

}
