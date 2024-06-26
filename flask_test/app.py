from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    data = request.json
    text = data.get("text")
    # 여기에 텍스트 분석 로직 추가
    response = {"sentiment": "positive", "text": text}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)