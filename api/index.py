from http.server import BaseHTTPRequestHandler
from xpinyin import Pinyin
from urllib.parse import urlparse, parse_qs

p = Pinyin()

instructions = """
<html>
  <head>
    <meta charset="utf-8">
    <style>
      body {
        font-family: sans-serif;
      }
    </style>
  </head>
  <body>
    Provide the hanzi GET parameter to use this API.<br/><br/>
    e.g. call https://pinyin.seve.blog/api?hanzi=你好<br/><br/>
    which is url encoded to http://localhost:3000/api?hanzi=%E4%BD%A0%E5%A5%BD
  </body>
</html>
""".strip()

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html; charset=utf-8')
        self.end_headers()
        qs = parse_qs(urlparse(self.path).query)

        if "hanzi" in qs:
          self.wfile.write(p.get_pinyin(qs["hanzi"][0], tone_marks="marks").encode("utf-8"))
          return

        self.wfile.write(instructions.encode("utf-8"))
        return
