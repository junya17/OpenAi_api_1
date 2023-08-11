from flask import Flask, request, jsonify, render_template
import openai, config 

app = Flask(__name__)

# OpenAIのAPIキーの設定
openai.api_key = config.OPENAI_API_KEY

@app.route('/', methods=['GET'])
def home():
        return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json['prompt']

    # OpenAIのAPIを使ってテキストを生成
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60
    )

    generated_text = response.choices[0].text
    print(f"Generated text: {generated_text}")  # これがコマンドラインに出力されます

    return jsonify(text=generated_text)
    


if __name__ == '__main__':
    app.run(debug=True)
