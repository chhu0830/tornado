import handlers.main as main
import handlers.users as users

urls = [
    (r"/", main.index),

    (r"/users", users.users),
    (r"/users/new", users.new_user),
    (r"/users/(\d+)/edit", users.edit_user),
    (r"/users/(\d+)", users.user)

]
