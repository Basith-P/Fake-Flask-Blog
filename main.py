from flask import Flask, render_template
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


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
