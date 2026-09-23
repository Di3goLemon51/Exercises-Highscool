public class Corso {
    
    // Assigning Variables
    private String nomeCorso;
    private String matricola;
    private int durataAnni;
    
    // Constructor
    public Corso(String nomeCorsoString, String matricolaString, int durataAnniInt) {
        this.nomeCorso = nomeCorsoString;
        this.matricola = matricolaString;
        this.durataAnni = durataAnniInt;
    }

    // Getters
    public String getNome() {
        return this.nomeCorso;
    }

    public String getMatricola() {
        return this.matricola;
    }

    public int getDurata() {
        return this.durataAnni;
    }

    // Setters
    public void setNome(String nomeCorsoString) {
        this.nomeCorso = nomeCorsoString;
    }

}
