from flask import (
    render_template, Blueprint, flash, g, redirect, request, url_for
)

from werkzeug.exceptions import abort

from myblog.models.post import Post
from myblog.models.user import User
from myblog.models.coment import Coment

from myblog.views.auth import login_required

from myblog import db 

blog = Blueprint('blog', __name__)


#obteniendo un usuario
def get_user(id):
    user = User.query.get_or_404(id)
    return user

#listar todos los posts
@blog.route('/')
def index():
    posts = Post.query.all()
    db.session.commit()
    return render_template('blog/index.html', posts = posts, get_user= get_user)

# Crear posts
@blog.route('/blog/create',methods=('GET','POST'))
@login_required
def register():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        
        post = Post(g.user.id, title, body)
        
        error = None
        
        if not title:
            error = 'Se requiere un titulo'
        
        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))

        flash(error)
        
    return render_template('blog/create.html')
    

