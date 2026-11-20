from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = 8000
APP_FOLDER = Path(__file__).resolve().parent

handler = partial(SimpleHTTPRequestHandler, directory=str(APP_FOLDER))

if __name__ == "__main__":
    print(f"Study game running at http://localhost:{PORT}")
    print("Press Ctrl+C to stop.")
    ThreadingHTTPServer(("127.0.0.1", PORT), handler).serve_forever()

