from app.server import app
import os

port = int(os.environ.get('PORT', 33507))
app.run(port=port,host='0.0.0.0')