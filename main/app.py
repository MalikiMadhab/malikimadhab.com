from flask import Flask, render_template
from pathlib import Path
import os

app = Flask(__name__)

PROJECT_PATH = Path(__file__).parent.parent.resolve()
DOMAIN = "malikimadhab.com"
CONTRIBUTORS = ["Sadi", "Rishan"]


@app.route("/")
def hello_world():
    try:
        readme_path = str(PROJECT_PATH / "main" / "README.md")
        if os.path.exists(readme_path):
            with open(readme_path, "r") as file:
                markdown_content = file.read()
        else:
            markdown_content = ""
    except Exception as exc:
        print(f"Server-side Error: {exc}")
    else:
        if markdown_content:
            return render_template("index.html", markdown_content=markdown_content)
        else:
            return f"""
                <h1> Welcome to {DOMAIN}! 😎</h1>
                <h3>This website is maintained by:<h3>
                <div>{" 🙌 ".join(CONTRIBUTORS)}</div>
                <h2>Do come back again. 👋</h2>
            """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
