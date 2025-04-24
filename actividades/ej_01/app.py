from microdot import Microdot
from microdot import send_file

app = Microdot()


@app.route('/')
def index(request):
    return send_file('index.html', content_type='text/html')  # in seconds

@app.route('/styles/base.css')
def css(request):
    return send_file('styles/base.css', content_type='text/css')  # in seconds

@app.route('/scripts/base.js')
def css(request):
    return send_file('scripts/base.js', content_type='text/css')  # in seconds


app.run(debug=True)