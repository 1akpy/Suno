from http.server import BaseHTTPRequestHandler
import urllib.request
import json

class handler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body   = json.loads(self.rfile.read(length))
        url    = body.get("url", "").strip()

        try:
            api_url = "https://opensuno.vercel.app/track?url=" + urllib.parse.quote(url, safe="")
            req  = urllib.request.Request(
                api_url,
                headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"},
            )
            resp = urllib.request.urlopen(req, timeout=12)
            data = json.loads(resp.read())
            result = json.dumps(data).encode()
        except Exception as e:
            result = json.dumps({"status": "error", "message": str(e), "data": None}).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self._cors()
        self.end_headers()
        self.wfile.write(result)

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin",  "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

import urllib.parse
