# Low Balancer

## Description:

> I built a reverse system with strong load balancer!

> Hack me if you can!

## Solution:

`setHeader()` can be used to do CRLF injection, but `%0d%0a` will be filtered. This can be bypassed with `%E5%98%8D%E5%98%8A` or [similar ways](https://blog.innerht.ml/twitter-crlf-injection/).

The target is the backend API Handler，which can do out-of-band XXE, arbitrary read and listing.

```c
if(!body.isEmpty()) {
    byte[] b = body.getBytes();
    ByteArrayInputStream bs = new  ByteArrayInputStream(b);
    DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
    dbFactory.setNamespaceAware(true);
    DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
    Document doc = dBuilder.parse(bs);
    NodeList nodeList = doc.getElementsByTagName("txt");
    Node node = nodeList.item(0);
    String response = reverse(node.getTextContent());
    setHeaders(t);
    writeResponse(t, response);
}
```

To execute the solution:

```console
root@kali:~# python -m SimpleHTTPServer
root@kali:~# python solve.py
```

`FLAG{HTTP_Smuggl3ing_cooool_4nd_Id3a_fr0m_drunk_S3ct0r}`
