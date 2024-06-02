from sqladmin import ModelView

from app.models.models import Users


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.user_id, Users.username, Users.email, Users.created_date]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name_plural = 'Users'
    icon = 'fa-solid fa-user'
