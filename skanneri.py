from flask import Flask, request, render_template
import socket

app = Flask(__name__)

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        conn = sock.connect((target, port))
        return True
    except:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    open_ports = []
    target = ''
    if request.method == 'POST':
        target = request.form.get('ip')
        for port in [80, 5000]:
            if scan_port(target, port):
                open_ports.append(port)
    return render_template('index.html', target=target, open_ports=open_ports)

if __name__ == '__main__':
    app.run(debug=True)