from app import app, db, ma
from app.models.layout_model import LayoutModel,LayoutSchema

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Image': Image}
