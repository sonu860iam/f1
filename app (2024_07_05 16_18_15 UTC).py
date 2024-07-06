from interface import Interface
from model import Model

app = Interface()
model = Model()

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
