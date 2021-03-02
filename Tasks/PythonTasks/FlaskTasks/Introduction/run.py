from flask import Flask,render_template

app=Flask(__name__)
data = 'Hello Flask'
@app.route('/')
def index():
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)