# crappyuploader
A crappy HTTPS uploader with minimal TLS support for when you want to grab files from one host and get it to your own.

## v1.0 ##

Just a dumb uploader over TLS. Might be useful, probably won't be though. Works with Python 3.11.7.

## How to use it ##

1. Download crappyuploader.py
2. Ensure flask and gunicorn are installed (or whatever python WSGI server you want, doesn't need to be gunicorn...)
3. Run crappyuploader.py


For example:

```
git clone
pip3 install flask gunicorn (or apt install python-flask python-gunicorn)
python3 crappyuploader.py
```

Then access via **https://YOUR_IP_ADDRESS:5000** and enjoy your crappy uploads!

