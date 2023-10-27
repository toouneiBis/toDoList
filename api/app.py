```
from flask import Flask
import api.routes as routes

app = Flask(__name__)
routes.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

```
