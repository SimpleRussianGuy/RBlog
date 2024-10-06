import os 

class Config:
    SECRET_KEY = 'dev' # After testing, change to your real secret key 
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGHT = 16 * 1024 * 1024 # Max size of uploading objects
    ALLOWED_EXTENSIONS = {'png','jpeg','jpg', 'gif'} # Allowed type of files for uploading