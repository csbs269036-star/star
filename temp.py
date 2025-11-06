

from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    """Return a custom friendly HTTP greeting."""
    #return "Hi Everyone ! I am running through cloud shell"
    num=int(input("num"))
    if (num>0 & num<100):
        num=num+273
        print(f"Celius to Faherant: {num}")

if __name__ == "__main__":
    app_host = "http://127.0.0.1:8080"
    print(f"App host link: {app_host}")
    app.run(host="127.0.0.1", port=8080, debug=True)
