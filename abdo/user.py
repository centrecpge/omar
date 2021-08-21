from flask import Blueprint,render_template,session,redirect,url_for
from .extensions import *
user=Blueprint('user','__name__',url_prefix='/user')#,template_folder='templates/views')


@user.before_request
def before():
	global us,A
	if not('user' in session) :
		return redirect(url_for('main.home'))
	else:
		us=Users.get(session['user'])
		A=[f.user_2 for f in Friends.query.filter_by(user_1=us.id)]
		A.extend([f.user_1 for f in Friends.query.filter_by(user_2=us.id)])

@user.context_processor
def context_processor():
	return dict(Title="X7max",Header='Abderafie_buildozer')
		

@user.route('/home',methods=['GET','POST'])
def Main():
	print(us)
	return render_template('user/home.html',user=us)


@user.route('/logout',methods=['GET','POST'])
def logout():
	session.pop('user')
	return redirect(url_for('main.home'))

@user.route('/users',methods=['GET','POST'])
def users():
	users=Users.query.all()
	users.remove(us)
	users=[user for user in users if not(user.id in A)]
	return render_template('user/users.html',users=users)

@user.route('/friends',methods=['GET','POST'])
def friends():
	users=Users.query.all()
	users.remove(us)
	users=[user for user in users if user.id in A]
	return render_template('user/friends.html',users=users)

@user.route('/msg<int:id>',methods=['GET','POST'])
def msg(id):
	session['user_2']=id
	return redirect(url_for('user.messages'))

@user.route('/messages',methods=['GET','POST'])
def messages():
	form = Message()
	if not ('user_2' in session):
		return redirect(url_for('user.friends'))
	try:
		F=Friends.get(us.id,session['user_2'])
	except:
		return redirect(url_for('user.friends'))
	if form.validate_on_submit():
		db.session.add(Messages(content=form.content.data,user_id=us.id,friends_id=F.id))
		db.session.commit()
	
	uss=Users.get(Friends.other(F,us.id))
	return render_template('user/messages.html',uss=uss,F=F,us=us,form=form,Users=Users)

@user.route('/posts',methods=['GET','POST'])
def posts():
	form=Post()
	if form.validate_on_submit():
		db.session.add(Posts(content=form.content.data,user_id=us.id))
		db.session.commit()
	return render_template('user/posts.html',form=form,us=us,Users=Users,Posts=Posts.query.all())

@user.route('/invitez<int:id>',methods=['GET','POST'])
def invite(id):
	db.session.add(Friends(user_1=us.id,user_2=id))
	db.session.commit()
	return redirect(url_for('user.users'))

	# def get(cls, u1,u2):
	# 	A=[F for F in Friends.query.filter_by(user_1=u1).all() if F.user_2==u2 ]
	# 	A.extend([F for F in Friends.query.filter_by(user_2=u1).all() if F.user_1==u2 ])
	# 	return A	