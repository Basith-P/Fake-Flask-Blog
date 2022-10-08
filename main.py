from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    posts = requests.get(posts_url).json()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post_url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    post = requests.get(post_url).json()
    return render_template('post.html', post=post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data)
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)


if __name__ == '__main__':
    app.run(debug=True)
