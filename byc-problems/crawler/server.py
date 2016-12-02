from flask import Flask, render_template, request
#import GeoIP

app = Flask(__name__, static_url_path='')

#@app.route('/')
#def index():
#  return render_template('index.html')

#@app.route('/')
#def root():
#  return app.send_static_file('robots.txt')

#@app.route('/server/<path:path>')
#def static_file(path):
#    return app.send_static_file(path)

@app.route('/')
def root():
  return app.send_static_file('index.html')

if __name__ == '__main__':
  app.run(debug = True)
