import logging
import transaction
from pyramid.view import view_config
from ..models.services.goat_service import GoatService
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..forms.forms import GoatCreateForm, GoatUpdateForm
from ..models.meta import DBSession
from ..models.goat import Goat

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
def goat_create(request):
    entry = Goat()
    form = GoatCreateForm(request.POST)
    form.breed.query_factory = GoatService.all_breed
    form.gender.query_factory = GoatService.all_gender
    form.father.query_factory = GoatService.bucks
    form.mother.query_factory = GoatService.goats
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        DBSession.add(entry)
        return HTTPFound(location=request.route_url('home'))
    return {'form': form, 'action': request.matchdict.get('action')}


@view_config(route_name='goat_action', match_param='action=edit',
             renderer='goat_database:templates/edit_goat.jinja2')
def goat_update(request):
    goat_id = int(request.params.get('id', -1))
    entry = GoatService.by_id(goat_id)
    if not entry:
        return HTTPNotFound()
    form = GoatUpdateForm(request.POST, entry)
    form.breed.query_factory = GoatService.all_breed
    form.gender.query_factory = GoatService.all_gender
    form.father.query_factory = GoatService.bucks
    form.mother.query_factory = GoatService.goats
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        return HTTPFound(location=request.route_url('goat', id=entry.id))
    return {'form': form, 'action': request.matchdict.get('action')}


@view_config(route_name='goat_action', match_param='action=delete')
def goat_delete(request):
    goat_id = int(request.params.get('id', -1))
    entry = GoatService.by_id(goat_id)
    if not entry:
        return HTTPNotFound()
    DBSession.delete(entry)
    transaction.commit()
    return HTTPFound(location=request.route_url('home'))
