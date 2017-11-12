from app import db

class Guest(db.Model):
  __tablename__ = 'guests'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(250), nullable=False)
  last_name = db.Column(db.String(250), nullable=False)
  additional_guest = db.Column(db.Boolean, default=False)
  ag_first_name = db.Column(db.String(250))
  ag_last_name = db.Column(db.String(250))

  def __repr__(self):
    return "<User(first_name={0}, last_name={1}, additional_guest={2}".format(
      self.first_name, self.last_name, self.additional_guest)

  @property
  def serialize(self):
    #Returns object data in easily serializable format
    return {
      'id': self.id,
      'first_name': self.first_name,
      'last_name': self.last_name,
      'additional_guest': self.additional_guest,
      'ag_first_name': self.ag_first_name,
      'ag_last_name': self.ag_last_name,
    }

db.create_all()