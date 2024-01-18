import os
from flask import Flask
import dotenv
from framework.delivery import Delivery


app = Flask(__name__)
delivery = Delivery(app).delivery_http()
dotenv.load_dotenv()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ['PORT']), debug=True)
