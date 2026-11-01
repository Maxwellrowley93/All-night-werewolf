# Serves the game locally for test.html, telling the browser never to keep an old copy of a file.
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = 8123


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()


if __name__ == '__main__':
    handler = partial(NoCacheHandler, directory=str(Path(__file__).parent))
    print(f'Open http://localhost:{PORT}/test.html')
    ThreadingHTTPServer(('localhost', PORT), handler).serve_forever()
