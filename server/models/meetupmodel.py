from db import db
import sqlite3


class MeetupModel(db.Model):
    __tablename__ = "Meetups"

    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    subtitle = db.Column(db.String(80))
    address = db.Column(db.String(80))
    imageurl = db.Column(db.String(200))
    email = db.Column(db.String(80))



    @classmethod
    def find_by_id(cls, this_id):
        return cls.query.filter_by(id_=this_id).first()

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def update_to_db(self,title:str):
        conn = sqlite3.connect("test.db")
        curs = conn.cursor()
        query = "UPDATE Meetups SET title=?, subtitle=?, address=?, imageurl=?, email=? where title=?"
        curs.execute(
            query,
            (
                self.title,
                self.subtitle,
                self.address,
                self.imageurl,
                self.email,
                self.title,
            ),
        )
        conn.commit()
        conn.close()
