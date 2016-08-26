from models import Service
from tornado import web, gen

class users(web.RequestHandler):
  @gen.coroutine
  def get(self):
    users = yield from Service.User.all("ORDER BY id DESC")
    self.render('users/index.html', users=users)

  @gen.coroutine
  def post(self):
    data=dict(
      email             = self.get_argument('email'),
      encrypted_password= self.get_argument('password'),
      current_sign_in_ip= self.request.remote_ip,
      last_sign_in_ip   = self.request.remote_ip
    )
    yield from Service.User.create(data)
    self.redirect('/users')

class new_user(web.RequestHandler):
  def get(self):
    self.render('users/new.html')

class edit_user(web.RequestHandler):
  @gen.coroutine
  def get(self, id):
    user = yield from Service.User.find(id)
    self.render('users/edit.html', user=user)

class user(web.RequestHandler):
  @gen.coroutine
  def get(self, id):
    user = yield from Service.User.find(id)
    self.render('users/show.html', user=user)

  @gen.coroutine
  def patch(self, id):
    print("123")
    data=dict(
      email="chhu0803@gmail.com"
    )
    yield from Service.User.update(data)
    self.redirect("/users/%d", id)
