from pyramid.view import view_config
from ..models.services.goat_service import GoatService
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..forms.forms import GoatCreateForm
from ..models.meta import DBSession
from ..models.goat import Goat
import logging
log = logging.getLogger(__name__)


@view_config(route_name='goat',
             renderer='goat_database:templates/goat.jinja2')
def goat_page(request):
    goat_id = int(request.matchdict.get('id', -1))
    entry = GoatService.by_id(goat_id)
    if not entry:
        return HTTPNotFound()
    return {'entry': entry}


@view_config(route_name='goat_action', match_param='action=create',
             renderer='goat_database:templates/edit_goat.jinja2')
def blog_create(request):
    entry = Goat()
    form = GoatCreateForm(request.POST)
    form.breed.query_factory = GoatService.all_breed
    form.gender.query_factory = GoatService.all_gender
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        entry.breed_id = form.breed.data.breed_id
        entry.gender_id = form.gender.data.gender_id
        DBSession.add(entry)
        return HTTPFound(location=request.route_url('home'))
    return {'form': form, 'action': request.matchdict.get('action')}


@view_config(route_name='goat_action', match_param='action=edit',
             renderer='goat_database:templates/edit_blog.jinja2')
def blog_update(request):
    return {}
