from flask import Flask

app = Flask(__name__)

DOMAIN = "malikimadhab.com"
CONTRIBUTORS = [
    "Sadi", "Rishan"
]

@app.route('/')

def hello_world():

    return f"""
    <h1> Welcome to {DOMAIN}! 😎</h1>
    <h3>This website is maintained by:<h3>
    <div>{" 🙌 ".join(CONTRIBUTORS)}</div>
    <h2>Do come back again. 👋</h2>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
