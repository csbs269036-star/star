from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def greet():
    """Return a custom friendly HTTP greeting with temperature conversion."""
    num = request.args.get("num", type=int)  # get ?num= value from URL
    message = "Hi Everyone! I am running through cloud shell. "

    if num is not None and num > 0 and num < 100:
        kelvin = num + 273
        fahrenheit = (num * 9/5) + 32
        message += f"Celsius: {num}, Kelvin: {kelvin}, Fahrenheit: {fahrenheit}"
    else:
        message += "Please provide a Celsius value between 0 and 100 using ?num= in the URL."

    return message

if __name__ == "__main__":
    app_host = "http://127.0.0.1:8080"
    print(f"App host link: {app_host}")
    app.run(host="127.0.0.1", port=8080, debug=True)
