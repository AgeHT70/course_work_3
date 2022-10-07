from flask import Blueprint, jsonify
from app.posts.dao.posts_dao import PostsDAO
from config import POSTS_PATH, COMMENTS_PATH
from logger import logger

api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao = PostsDAO(POSTS_PATH, COMMENTS_PATH)


@api_blueprint.route('/api/posts')
def api_posts() -> list:
    posts = posts_dao.get_all()
    logger.info(f"Запрос /api/posts")
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def api_post_by_pk(post_id) -> dict:
    post = posts_dao.get_by_pk(post_id)
    logger.info(f"Запрос /api/posts/{post_id}")
    return jsonify(post)
