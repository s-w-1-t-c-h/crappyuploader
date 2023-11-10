# crappyuploader
A crappy HTTPS uploader with minimal TLS support for when you want to grab files from one host and get it to your own. Might be useful, probably won't be though. Works with Python 3.11.7.

![image](https://github.com/s-w-1-t-c-h/crappyuploader/assets/6980812/3a791ff1-ddb3-4c4a-97cc-c3ed28746b18)

See? Just like that.

## v1.0 ##

1. Download crappyuploader.py
2. Ensure flask and gunicorn are installed (or whatever python WSGI server you want, doesn't need to be gunicorn...)
3. Run crappyuploader.py

For example:

```
git clone https://github.com/s-w-1-t-c-h/crappyuploader.git
pip3 install flask gunicorn (or apt install python-flask python-gunicorn)
python3 crappyuploader.py
```

Then access via **https://YOUR_IP_ADDRESS:5000** and enjoy your crappy uploads! Swap out the random PEM files for your own if you want to avoid the old cert warnings.

![image](https://github.com/s-w-1-t-c-h/crappyuploader/assets/6980812/fb17bac8-b2cf-4862-9771-080ceaf94752)
