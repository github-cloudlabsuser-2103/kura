from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def disk_usage():
    # Run the PowerShell script and capture the output
    output = subprocess.check_output(['powershell.exe', '.\\monit.ps1'], shell=True)

    # Decode the output and replace newline characters with HTML breaks
    output = output.decode('utf-8').replace('\n', '<br>')

    return output
#jee huu
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)