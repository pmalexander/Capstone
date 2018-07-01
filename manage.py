import os
from flask_script import Manager
from w import app
from flask_migrate import Migrate, MigrateCommand
from w.database import Base

from w.database import Location, Fauna, Feature, Flora

from w.dataseed import read_rawdata

manager = Manager(app)
#look over this, this will be written by the Session() on line 21 below, or rather whatever gps app works nowadays
#session = gps.gps()

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    print('test')

#seeds raw data contained within src file to populate database
@manager.command
def seed():
    print('Anything')
    locations = read_rawdata("./w/seed/location.src", ",")
    faunas = read_rawdata("./w/seed/fauna.src", "#")
    floras = read_rawdata("./w/seed/flora.src", "#")
    features = read_rawdata("./w/seed/feature.src", "#")
    
    print('\n\n\n\n\n\n')

    for location in locations:
#        print(location)
        obj = Location(**location)
        obj.latitude=float(location['latitude'])
        obj.longitude=float(location['longitude'])
        obj.visitors=int(location['visitors'])
        session.add(obj)
        session.commit()

    for fauna in faunas:
#        print(fauna)
        obj = Fauna(**fauna)
        session.add(obj)
        session.commit()
        
    for flora in floras:
#        print(flora)
        obj = Flora(**flora)
        session.add(obj)
        session.commit()
        
    for feature in features:
#        print(feature)
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

