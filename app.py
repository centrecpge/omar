import abdo
app=abdo.create_app()
if __name__ == '__main__':
	app.run(debug=True)



@app.context_processor
def context_processor():
	return dict(Title="X7max",Header='Abderafie_buildozer')




