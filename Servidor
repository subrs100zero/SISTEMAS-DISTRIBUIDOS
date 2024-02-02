import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ConversorMoeda extends Remote {
    double euroParaReal(double valorEuro) throws RemoteException;
    double realParaEuro(double valorReal) throws RemoteException;
    double dolarParaReal(double valorDolar) throws RemoteException;
    double realParaDolar(double valorReal) throws RemoteException;
}






import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ServidorConversorMoeda extends UnicastRemoteObject implements ConversorMoeda {

    public ServidorConversorMoeda() throws RemoteException {
        super();
    }

    @Override
    public double euroParaReal(double valorEuro) throws RemoteException {
        // Implemente a lógica de conversão Euro para Real aqui
        return valorEuro * 6.25; // Valor fictício para exemplo
    }

    @Override
    public double realParaEuro(double valorReal) throws RemoteException {
        // Implemente a lógica de conversão Real para Euro aqui
        return valorReal / 6.25; // Valor fictício para exemplo
    }

    @Override
    public double dolarParaReal(double valorDolar) throws RemoteException {
        // Implemente a lógica de conversão Dolar para Real aqui
        return valorDolar * 5.50; // Valor fictício para exemplo
    }

    @Override
    public double realParaDolar(double valorReal) throws RemoteException {
        // Implemente a lógica de conversão Real para Dolar aqui
        return valorReal / 5.50; // Valor fictício para exemplo
    }

    public static void main(String[] args) {
        try {
            ServidorConversorMoeda servidor = new ServidorConversorMoeda();
            java.rmi.registry.LocateRegistry.createRegistry(1099);
            java.rmi.Naming.rebind("ConversorMoeda", servidor);
            System.out.println("Servidor pronto para receber solicitações...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
