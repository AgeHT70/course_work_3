from flask import render_template, Blueprint, request, redirect

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


@bookmarks_blueprint.route('/bookmarks')
def bookmarks_page():
    #  Для переадресации (редиректа) используйте
    return redirect("/", code=302)

# bookmarks/remove/postid
# bookmarks/add/postid