import java.io.*;
import java.net.*;
import javax.swing.*;

public class server {
    public static void main(String[] args) throws Exception {
        ServerSocket ss = new ServerSocket(5000);
        System.out.println("Server waiting...");
        Socket s = ss.accept();
        DataInputStream in = new DataInputStream(s.getInputStream());
        String fname = in.readUTF();
        long len = in.readLong();

        FileOutputStream f = new FileOutputStream(fname);
        byte[] buf = new byte[4096];
        long r = 0;
        while (r < len) {
            int n = in.read(buf, 0, (int)Math.min(buf.length, len - r));
            if (n == -1) break;
            f.write(buf, 0, n);
            r += n;
        }
        f.close();
        System.out.println("Image saved: " + fname);

        JFrame fr = new JFrame("Received Image");
        fr.add(new JLabel(new ImageIcon(fname)));
        fr.setSize(500, 400);
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setVisible(true);

        s.close();
        ss.close();
    }
}
