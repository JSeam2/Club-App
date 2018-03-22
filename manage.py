from app import app

def runserver():
    """Run server"""
    app.run(debug=True)

if __name__ == "__main__":
    runserver()
