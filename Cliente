import java.rmi.Naming;

public class ClienteConversorMoeda {
    public static void main(String[] args) {
        try {
            ConversorMoeda conversor = (ConversorMoeda) Naming.lookup("rmi://localhost/ConversorMoeda");

            // Exemplo de uso
            double valorEuro = 100.0;
            double valorReal = conversor.euroParaReal(valorEuro);
            System.out.println(valorEuro + " Euros equivalem a " + valorReal + " Reais.");

            double valorDolar = 50.0;
            double valorRealDolar = conversor.dolarParaReal(valorDolar);
            System.out.println(valorDolar + " Dólares equivalem a " + valorRealDolar + " Reais.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
