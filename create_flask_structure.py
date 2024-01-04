import os

# Define the directory structure
directories = [
    "app/templates",
    "app/static",
    "app"
]

# Define files to create
files = {
    "app/__init__.py": (
        "from flask import Flask\n"
        "app = Flask(__name__)\n\n"
        "from app import routes\n"
    ),
    "app/routes.py": (
        "@app.route('/')\n"
        "def home():\n"
        "    return 'Hello, World!'\n"
    ),
    "run.py": (
        "from app import app\n\n"
        "if __name__ == '__main__':\n"
        "    app.run(debug=True)\n"
    ),
    "requirements.txt": "flask\n"
}

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, 'w') as file:
        file.write(content)

print("Flask project structure created successfully.")
