from flask import Blueprint,render_template,session,redirect,url_for
from .extensions import *
admin=Blueprint('admin','__name__',url_prefix='/admin')#,template_folder='templates/views')




@admin.before_request
def before():
	print(session)
	if not('admin' in session) :
		return redirect(url_for('main.login'))
	else:
		user=User.get(session['admin'])#à retour pour modifier

@admin.route('/logout',methods=['GET','POST'])
def logout():
	session.pop('admin')
	print('logout')
	print(session)
	return 'logout admin seccuss'

@admin.route('/',methods=['GET','POST'])
def Main_abdo():
	print('dashboard admin')
	print(session)
	return render_template('views/home.html',Title='Classification GTR abderafie chairi')
