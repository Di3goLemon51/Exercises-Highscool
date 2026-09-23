import java.util.ArrayList;
import java.util.List;

public class Docente {

    private List<Object> corsi = new ArrayList<Object>();

    // Constructor
    public Docente(List<Object> corsiList) {
        this.corsi = corsiList;
    }

    // Getters
    public void getCorsi() {
        for (Object corso : corsi) {
            // System.out.println( corso.nomeCorso + " " + corso.matricola + " " + corso.durataAnni);
        }
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
