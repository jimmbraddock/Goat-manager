import logging
import shutil
import os

import transaction
from pyramid.view import view_config
from ..models.services.goat_service import GoatService
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..forms.forms import GoatCreateForm, GoatUpdateForm
from ..models.meta import DBSession
from ..models.goat import Goat
from pyramid.path import AssetResolver

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

    form.photo.widget.img = '{0}/static/img/goat_photos/{1}/{2}'.format(request.application_url, entry.name,
                                                                        entry.photo_path)
    if request.method == 'POST' and form.validate():
        image_data = request.POST[form.photo.id].file
        filename = request.POST[form.photo.id].filename
        print(image_data)

        a = AssetResolver()
        resolver = a.resolve('goat_database:static/img/goat_photos/')
        print(resolver.abspath())
        path = os.path.join(resolver.abspath(), form.name.data)
        print(path)
        temp_file_path = os.path.join(path, filename)
        print(temp_file_path)
        os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
        image_data.seek(0)
        with open(temp_file_path, 'wb+') as output_file:
            shutil.copyfileobj(image_data, output_file)

        # open(os.path.join(UPLOAD_PATH, form.photo.data), 'w').write(image_data)

        entry.photo_path = filename
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
    # delete image from server

    transaction.commit()
    return HTTPFound(location=request.route_url('home'))
