from flask import (
    render_template, Blueprint, redirect, g, request, url_for
)

from myblog.models.coment import Coment
from myblog import db 
from myblog.views.auth import login_required
from myblog.models.user import User
from myblog.models.post import Post

comentario = Blueprint('comentario', __name__)

def get_user(id):
    user = User.query.get_or_404(id)
    return user

# Listar todos los comentarios
@comentario.route('/', methods=['POST'])
def comentario_create():
    if request.method == 'POST':
        body = request.form.get('body')
        author = g.user.username  # Obtener el usuario actual
        post_id = request.form.get('post_id')  # Obtener el ID del post desde el formulario

        coment = Coment(author=author, body=body, post_id=post_id)
        db.session.add(coment)
        db.session.commit()

        # Obtener todos los comentarios asociados a un post específico
        coments = Coment.query.filter_by(post_id=post_id).all()

        return render_template('blog/index.html', coments=coments, user=g.user)

    return redirect(url_for('blog.index'))
