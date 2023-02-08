from flask import Flask, render_template, request
import config

app = Flask(__name__)

@app.route('/top-50')
def top_50():
    return render_template('index.html', title='Top 50', song=config.get_popular())

if __name__ == '__main__':
    app.run(debug=True)