from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    result = None
    if request.method == 'POST':
        budget = request.form.get('budget')
        category = request.form.get('category')
        need = request.form.get('need')
        result = f"Budget {budget} ku Best {category} for {need} - WORKING DA!"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
