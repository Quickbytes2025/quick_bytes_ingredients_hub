# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .categories import category_views
from .recipe import recipe_views
from .admin import setup_admin


views = [user_views, index_views, auth_views, category_views, recipe_views] 
# blueprints must be added to this list