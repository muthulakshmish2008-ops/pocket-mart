from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key="YOUR_API_KEY")

@app.route('/', methods=['GET','POST'])
def home():
    answer = ""
    if request.method == 'POST':
        budget = request.form.get('budget')
        category = request.form.get('category')
        need = request.form.get('need')
        prompt = f"Budget {budget}, category {category}, need {need}. Recommend best products from Amazon, Flipkart, IKEA within budget."
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            answer = response.text
        except:
            answer = f"Best for {budget} in {category}: Check Amazon, Flipkart, IKEA"
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)