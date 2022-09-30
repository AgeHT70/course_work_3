from flask import Blueprint, jsonify
from app.posts_bp.dao.posts_dao import PostsDAO


api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao = PostsDAO("./data/posts.json")


@api_blueprint.route('/api/posts')
def api_posts():
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def api_post_by_pk(post_id):
    post = posts_dao.get_by_pk(post_id)
    return jsonify(post)
