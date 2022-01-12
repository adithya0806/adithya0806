from flask import Flask

app = Flask(__name__)

@app.route("/<int:n>")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#n=int(input("Input a number to compute the factiorial : "))
#print(factorial(n))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
