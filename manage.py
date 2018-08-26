import os
from flask_script import Manager
from w import app
from flask_migrate import Migrate, MigrateCommand
from w.database import Base

from w.database import Location, Fauna, Feature, Flora

from w.dataseed import read_rawdata

from w.database import User
import getpass


manager = Manager(app)
#look over this, this will be written by the Session() on line 21 below, or rather whatever gps app works nowadays
#session = gps.gps()

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

@manager.command
def adduser():
    name = input("User's name: ")

    while True:
        email = input("Email: ")
        user = session.query(User).filter_by(email=email).first()
        if user:
            print("this email is already in use, choose another")
        else:
            break

    password = getpass.getpass(prompt="password: ")

    new_user = User()
    new_user.name = name
    new_user.email = email
    new_user.password = generate_password_hash(password)

    session.add(new_user)
    session.commit()
    print("user added successfully")
    

@manager.command
def test():
    print('test')

#seeds raw data contained within src file to populate database
@manager.command
def seed():
    locations = read_rawdata("./w/seed/location.src", ",")
    faunas = read_rawdata("./w/seed/fauna.src", "#")
    floras = read_rawdata("./w/seed/flora.src", "#")
    features = read_rawdata("./w/seed/feature.src", "#")
    
#creates space needed to parse information produced when debugging    print('\n\n\n\n\n\n')

    for location in locations:
#used as a means to debugging, showing location keys and values        print(location)
        obj = Location(**location)
        obj.latitude=float(location['latitude'])
        obj.longitude=float(location['longitude'])
        obj.visitors=int(location['visitors'])
        session.add(obj)
        session.commit()

    for fauna in faunas:
#used as a means to debugging, showing fauna keys and values        print(fauna)
        obj = Fauna(**fauna)
        session.add(obj)
        session.commit()
        
    for flora in floras:
#used as a means to debugging, showing flora keys and values        print(flora)
        obj = Flora(**flora)
        session.add(obj)
        session.commit()
        
    for feature in features:
#used as a means to debugging, showing feature keys and values        print(feature)
        obj = Feature(**feature)
        session.add(obj)
        session.commit()

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

from w.database import session

if __name__ == "__main__":
    manager.run()

