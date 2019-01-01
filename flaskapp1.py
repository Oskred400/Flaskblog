#blog posts web app

from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author' : 'Oskred',
        'title' : 'Blogs',
        'content' : 'First Post',
        'date_posted': 'December 30, 2018'

    },
    {
        'author' : 'Oskred100',
        'title' : 'Blog2',
        'content' : 'Second Post',
        'date_posted' : 'December 30, 2018'

    }
]




@app.route("/")
def hello():
    return render_template('home.html', posts = posts)

@app.route("/about")

def about():
    return render_template('about.html', title = 'About')

#@app.route("/Signup")

#def signup():
#    return ,

@app.route("/authors")
def authors():
    return render_template('authors.html', title = 'Authors', posts = posts)



if __name__ == "__main__":
    app.run(port=1000, debug = True)
