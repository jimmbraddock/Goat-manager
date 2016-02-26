from pyramid.view import view_config
from ..models.services.goat_service import GoatService


@view_config(route_name='goat',
             renderer='goat_database:templates/goat.jinja2')
def goat_page(request):
    goat_id = int(request.matchdict.get('id', -1))
    entry = GoatService.by_id(goat_id)
    if not entry:
        return HTTPNotFound()
    return {'entry': entry}
