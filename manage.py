from app import app_factory
import os

app = app_factory(os.environ.get("MODE_CONFIG") or "default")

if __name__ == "__main__":
    app.run(host='0.0.0.0')