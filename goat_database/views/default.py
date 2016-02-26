from pyramid.view import view_config
from ..models.services.goat_service import GoatService


@view_config(route_name='home',
             renderer='goat_database:templates/index.jinja2')
def index_page(request):
    goats = GoatService.all()
    print(goats)
    return {'goats': goats}
