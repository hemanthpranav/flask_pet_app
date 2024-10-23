from flask import Flask, render_template, redirect, url_for, flash
from models import db, Pet
from forms import PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pet_manager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, type=form.type.data, age=form.age.data)
        db.session.add(new_pet)
        db.session.commit()
        flash('Pet added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('view_pets.html', form=form)

@app.route('/delete_pet/<int:pet_id>', methods=['POST'])

def add_type():
    if request.method == 'POST':
        type_name = request.form['name']

        new_type = PetType(name=type_name)
        db.session.add(new_type)
        db.session.commit()

        flash('Pet type added successfully!')
        return redirect(url_for('index'))

    return render_template('add_type.html')
    
def delete_pet(pet_id):
    pet_to_delete = Pet.query.get_or_404(pet_id)
    db.session.delete(pet_to_delete)
    db.session.commit()
    flash('Pet deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
