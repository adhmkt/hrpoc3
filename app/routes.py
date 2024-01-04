from app import app

@app.route('/')
def home():
    return 'Hello, World! I will learn how to do this.'

