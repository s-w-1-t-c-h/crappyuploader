from flask import Flask, render_template_string, request
import ssl
import os
import logging

app = Flask(__name__)

# Directory to store uploaded files
UPLOADS_DIR = 'uploads'

# HTML template
html_template = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  
  <title>File Uploader</title>
  <!-- Your styles here -->
</head>
<body>
  <div class="container">
    <div class="jumbotron">
    <pre>
   _____                               _    _       _                 _           
  / ____|                             | |  | |     | |               | |          
 | |     _ __ __ _ _ __  _ __  _   _  | |  | |_ __ | | ___   __ _  __| | ___ _ __ 
 | |    | '__/ _` | '_ \| '_ \| | | | | |  | | '_ \| |/ _ \ / _` |/ _` |/ _ | '__|
 | |____| | | (_| | |_) | |_) | |_| | | |__| | |_) | | (_) | (_| | (_| |  __| |   
  \_____|_|  \__,_| .__/| .__/ \__, |  \____/| .__/|_|\___/ \__,_|\__,_|\___|_|   
                  | |   | |     __/ |        | |                                  
                  |_|   |_|    |___/         |_|                                  

              		"Now with even crappier TLS support!"

v1.0 by sw1tch 2023
--------------------------------------------------------------------------------
</pre>
    	<form method="POST" action="/upload" enctype="multipart/form-data">
        <div class="form-group">
          <label for="file">Choose a file</label>
          <input type="file" class="form-control-file" name="file" id="file" required>
        </div>
        <button type="submit" class="btn btn-primary">Upload</button>
      </form>
    </div>
    <div class="small-text">
      <p><b>Server:</b> {{ hostname }}<br>
      <b>Client:</b> {{ client_ip }}</p>
    </div>
  </div>
</body>
</html>
"""

def generate_self_signed_certificate():
    cert_file = 'cert.pem'
    key_file = 'key.pem'

    if not (os.path.isfile(cert_file) and os.path.isfile(key_file)):
        print(f"[*] No crappy certs available...generating some for you!")
        # Generate a self-signed certificate and key silently
        os.system(f"openssl req -x509 -newkey rsa:4096 -keyout {key_file} -out {cert_file} -days 90 -nodes -subj '/CN=crappylocalhost' > /dev/null 2>&1")
    else:
        print(f"[*] Certificate files already exist, it seems! Hope they aren't crappy...")

    return cert_file, key_file

@app.route('/')
def index():
    hostname = request.host.split(':')[0]
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    return render_template_string(html_template, hostname=hostname, client_ip=client_ip)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # Ensure the 'uploads' directory exists
    os.makedirs(UPLOADS_DIR, exist_ok=True)

    # Save the file in the 'uploads' directory
    file_path = os.path.join(UPLOADS_DIR, file.filename)
    file.save(file_path)

    return f'File uploaded successfully to {file_path}'

if __name__ == '__main__':

    ascii_art = """
   _____                               _    _       _                 _           
  / ____|                             | |  | |     | |               | |          
 | |     _ __ __ _ _ __  _ __  _   _  | |  | |_ __ | | ___   __ _  __| | ___ _ __ 
 | |    | '__/ _` | '_ \| '_ \| | | | | |  | | '_ \| |/ _ \ / _` |/ _` |/ _ | '__|
 | |____| | | (_| | |_) | |_) | |_| | | |__| | |_) | | (_) | (_| | (_| |  __| |   
  \_____|_|  \__,_| .__/| .__/ \__, |  \____/| .__/|_|\___/ \__,_|\__,_|\___|_|   
                  | |   | |     __/ |        | |                                  
                  |_|   |_|    |___/         |_|                                  

v1.0 by sw1tch 2023
---------------------------------------------------------------------------------
"""
    print(ascii_art)
    cert_file, key_file = generate_self_signed_certificate()
    
    # Run Gunicorn with SSL
    command = f"gunicorn -w 4 -b 0.0.0.0:5000 --certfile={cert_file} --keyfile={key_file} crappyuploader:app"
    os.system(command)

