import java.io.*;
import java.net.*;

public class client {
    public static void main(String[] args) throws Exception {
        String url = "https://unsplash.com/photos/the-sun-is-setting-over-the-mountains-in-the-distance-RsCvxI9h2Ew";

        URL u = new URL(url);
        HttpURLConnection conn = (HttpURLConnection) u.openConnection();
        conn.setRequestProperty("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)");

        InputStream in = new BufferedInputStream(conn.getInputStream());
        ByteArrayOutputStream bout = new ByteArrayOutputStream();
        byte[] buf = new byte[4096];
        int n;
        while ((n = in.read(buf)) != -1) bout.write(buf, 0, n);
        in.close();
        byte[] img = bout.toByteArray();

        FileOutputStream f = new FileOutputStream("img.jpg");
        f.write(img);
        f.close();
        System.out.println("Image downloaded as img.jpg");

        Socket s = new Socket("localhost", 5000);
        DataOutputStream out = new DataOutputStream(s.getOutputStream());
        out.writeUTF("img.jpg");
        out.writeLong(img.length);
        out.write(img);
        out.close();
        s.close();
        System.out.println("Image sent to server successfully.");
    }
}
