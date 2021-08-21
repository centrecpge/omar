from flask import Blueprint,render_template,session,redirect,url_for
from .extensions import *
main=Blueprint('main','__name__',url_prefix='/main')#,template_folder='templates/views')

@main.context_processor
def context_processor():
	return dict(Title="X7max",Header='Abderafie_buildozer')



@main.route('/register',methods=['GET','POST'])
def register():
	form=Register()
	if form.validate_on_submit():
		if Users.query.filter_by(email=form.email.data).first():
			return render_template('views/home.html',warn=True,alert="Email already exists",form=form)
		db.session.add(Users(
			name=form.username.data,
			email=form.email.data,
			password=form.password.data
			))
		db.session.commit()
		return render_template('views/home.html',alert='validate on submit please login',Title='X7max')
	return render_template('views/register.html',form=form)


@main.route('/home',methods=['GET','POST'])
def home():
	# user=Users.get(2)
	# print(user.posts)
	return render_template('views/home.html')


@main.route('/login',methods=['GET','POST'])
def login():
	form=Login()
	# print(Users.query.all())
	if form.validate_on_submit():
		if Users.query.filter_by(email=form.email.data).first():
			User=Users.query.filter_by(email=form.email.data).first()
			if User.password==form.password.data:
				session['user']=User.id
				print(session)
				return redirect(url_for('user.Main'))
			else:
				return render_template('views/login.html',warn=True,alert='Password is not correct',form=form)
			return str(User.name)
		else :
			return render_template('views/login.html',warn=True,alert='email is not correct',form=form)
	return render_template('views/login.html',form=form)