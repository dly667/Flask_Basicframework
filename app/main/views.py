from datetime import datetime
from flask import render_template,session ,redirect,url_for

from . import main
# from .form import NameForm
from .. import db
<<<<<<< HEAD
# from ..models import User

=======
from ..models import User
print(db,22)
>>>>>>> 84b076b0435bb12be18ec6e37d872f9b3ccb3bb6
@main.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('.index'))
    return render_template('index.html',
            form = form,name=session.get('name'),
            known = session.get('known',False),
            current_time=datetime.utcnow())