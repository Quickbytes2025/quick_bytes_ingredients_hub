# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .categories import category_views
from .recipe import recipe_views
from .admin import setup_admin
from .i_user import i_user_views
from .ingredients import ingredient_views
from .r_user import r_user_views


views = [user_views, index_views, auth_views, category_views, recipe_views,i_user_views,ingredient_views,r_user_views] 
# blueprints must be added to this list