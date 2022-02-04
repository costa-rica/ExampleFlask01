from flask import Blueprint
from flask import render_template_string

bp = Blueprint('errors', __name__)

@bp.app_errorhandler(404)
def handle_404(err):
    return render_template_string("<h1>404 Error</h1><h2> Medium Sample App Custom Error Handler Page</h2>"),404
    
@bp.app_errorhandler(500)
def handle_500(err):
    return render_template_string("<h1>500 Error</h1><h2> Medium Sample App Custom Error Handler Page</h2>"),500