import os
from flask import Flask
import dotenv
from framework.delivery.http.http import delivery_http


app = Flask(__name__)
delivery_http(app)
dotenv.load_dotenv()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ['PORT']), debug=True)
