from flask import jsonify, render_template
from app import app


@app.route("/")
@app.route("/health-check")
def health_check():
    return jsonify(
        {
            "message": "Your app launched Successfully",
            "success": True
        }
    )


post_list = [
    {
        "id": 1,
        "author": "harish",
        "title": "Blog1",
        "description": "Bla,BLa,Bla,Bla,Bla"
    },
    {
        "id": 2,
        "author": "harish2",
        "title": "Blog2",
        "description": "Bla,BLa,Bla,Bla,Bla"
    },
    {
        "id": 3,
        "author": "harish3",
        "title": "Blog3",
        "description": "Bla,BLa,Bla,Bla,Bla"
    },
    {
        "id": 4,
        "author": "harish4",
        "title": "Blog4",
        "description": "Bla,BLa,Bla,Bla,Bla"
    }
]


@app.route("/posts")
def posts():
    return render_template("post_list.html", post_list=post_list)


@app.route("/posts/<int:id>")
def get_post(id):
    post = next((post for post in post_list if post.get('id') == id),None)
    if post:
        return render_template("post_detail.html", post=post)
    else:
        return "404 Post not found"