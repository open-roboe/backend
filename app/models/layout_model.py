from app import db,ma

class LayoutModel (db.Model):
    __tablename__ = 'layout_mymodel'
    id = db.Column('layout_id',db.Integer, primary_key=True)
    name =  db.Column(db.String(100))
    description = db.Column(db.String(255))
    parameters = db.Column(db.String())

    def __init__(self, name, description, parameters):
        self.name = name
        self.description = description
        self.parameters = parameters

class LayoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LayoutModel