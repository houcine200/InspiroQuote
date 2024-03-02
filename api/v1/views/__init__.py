from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.categories import *
from api.v1.views.quotes import *
from api.v1.views.authors import *
from api.v1.views.citations import *
from api.v1.views.users import *
from api.v1.views.reviews import *
