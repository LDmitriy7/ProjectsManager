from views import app
import config

app.run(host=config.APP_HOST, port=config.APP_PORT)

