from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()



class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(50),  nullable=False)
	posts = db.relationship('Posts', backref='users', lazy=True)
	messages = db.relationship('Messages', backref='users', lazy=True)
	@classmethod
	def get(cls, user_id):
		try:
			return Users.query.filter_by(id=user_id).one()
		except NoResultFound:
			return None
class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(120), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)

class Friends(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_1 = db.Column(db.Integer, nullable=False)
	user_2 = db.Column(db.Integer, nullable=False)
	messages = db.relationship('Messages', backref='friends', lazy=True)

	def other(self, user_id):
		if self.user_1==user_id:
			return self.user_2
		return self.user_1
	@classmethod
	def get(cls, u1,u2):
		A=Friends.query.filter_by(user_1=u1).filter_by(user_2=u2).all()
		A.extend(Friends.query.filter_by(user_1=u2).filter_by(user_2=u1).all())	
		return A[0]

class Messages(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(120), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
	friends_id = db.Column(db.Integer, db.ForeignKey('friends.id'),nullable=False)

# class Rules(db.Model):
# 	__tablename__ = 'rules'
# 	id = db.Column(db.Integer, primary_key=True)
# 	rule = db.Column(db.String(120), nullable=False)
# 	users = db.relationship('users', backref='rule', lazy=True)
	


#------------------full class User-----------------------
#from werkzeug.security import check_password_hash, generate_password_hash
# class User(db.Model, UserMixin):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(50), nullable=False)
#     name = db.Column(db.String(128), nullable=False)
#     email = db.Column(db.String(128), nullable=False, unique=True)
#     password = db.Column(db.String(54), nullable=False)
#     level = db.Column(db.Integer, nullable=False, default=10)
#     active = db.Column(db.SmallInteger, nullable=False, default=True)
#     addresses = db.relationship('Address')

#     created_at = db.Column(db.DateTime, default=db.func.now())
#     updated_at = db.Column(db.DateTime, onupdate=db.func.now())

#     def __init__(self, username, name, email, password):
#         self.username = username
#         self.name = name
#         self.email = email
#         self.set_password(password)

#     def __repr__(self):
#         return '<User %s>' % self.username

#     def set_password(self, password):
#         self.password = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password, password)

#     @classmethod
#     def get(cls, user_id):
#         """

#         :rtype: object
#         :type user_id: int
#         """
#         try:
#             return User.query.filter_by(id=user_id).one()
#         except NoResultFound:
#             return None

#---------------db commands--------------------------
# db.create_all()
# admin = User(username='admin', email='admin@example.com')
# db.session.add(guest)
# db.session.commit()
# User.query.all()
# User.query.filter_by(username='admin').first()



#------------relationship one to many-----------------------
# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     addresses = db.relationship('Address', backref='person', lazy=True)

# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), nullable=False)
#     person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
#         nullable=False)


