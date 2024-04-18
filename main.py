from flask import Flask, render_template, request
import requests
import json

url = "https://google.serper.dev/news"

headers = {
  'X-API-KEY': 'd8623ac935522b1125b44aea21f38328fb769fb5',
  'Content-Type': 'application/json'
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', article_title = "", article_snippet = "")

@app.route('/submit', methods=['POST'])
def submit():
    input_data = request.form['input_data']

    checkbox_value = request.form.get('checking_language')

    print("checked")

    # if checkbox_value == 'on':
    #     language = "kk"
    #     print("kk")
    # else:
    #     language = "ru"
    #     print("ru")

    payload = json.dumps({
        "q": input_data,
        "location": "Kazakhstan",
        "gl": "kz",
        "hl": "ru",
        "num": 20,
        "page": 3
        })

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.json()["news"] == []:
        return render_template("index.html", article_title = "", article_snippet = "Ничего не найдено!")
    else:
        return render_template("index.html", article_title = response.json()["news"][0]["title"], article_snippet = response.json()["news"][0]["snippet"])


if __name__ == '__main__':
    app.run(debug=True)
