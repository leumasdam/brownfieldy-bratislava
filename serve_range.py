#!/usr/bin/env python3
"""Statický server s podporou HTTP Range requestov — nutné pre pmtiles (model budov)."""
import http.server, os, re, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8099

class RangeHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        rng = self.headers.get('Range')
        if not rng:
            self.send_header  # no-op
            return super().do_GET()
        path = self.translate_path(self.path.split('?', 1)[0].split('#', 1)[0])
        if not os.path.isfile(path):
            return super().do_GET()
        size = os.path.getsize(path)
        m = re.match(r'bytes=(\d+)-(\d*)', rng)
        if not m:
            return super().do_GET()
        start = int(m.group(1))
        end = int(m.group(2)) if m.group(2) else size - 1
        end = min(end, size - 1)
        if start > end:
            self.send_error(416); return
        length = end - start + 1
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(path))
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.send_header('Content-Length', str(length))
        self.end_headers()
        with open(path, 'rb') as f:
            f.seek(start)
            self.wfile.write(f.read(length))

    def log_message(self, *a):  # tichšie logy
        pass

http.server.ThreadingHTTPServer.allow_reuse_address = True
with http.server.ThreadingHTTPServer(('', PORT), RangeHandler) as httpd:
    print(f'Range server na http://localhost:{PORT}')
    httpd.serve_forever()
