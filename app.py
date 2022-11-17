from flask import (render_template, 
                    url_for, request, redirect)
from models import db, Pet, app



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-pet', methods=['GET', 'POST'])
def add_pet():
    if request.form: #if there is no form to be submitted we send the user to addpet.html
        print(request.form)
        print(request.form['name'])
        new_pet = Pet(name=request.form['name'], age=request.form['age'], 
                        breed=request.form['breed'], color=request.form['color'],
                        size=request.form['size'], weight=request.form['weight'],
                        url=request.form['url'], url_tag=request.form['alt'],
                        pet_type=request.form['pet'], gender=request.form['gender'],
                        spay=request.form['spay'], house_trained=request.form['house_trained'],
                        desctription=request.form['desctription'])
        '''creates the Python object'''
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addpet.html')

@app.route('/pet')
def pet():
    return render_template('pet.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')