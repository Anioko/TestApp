class Opportunity(db.Model):
    __tablename__ = 'opportunities'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    title = db.Column(db.String)
    summary = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    available_now = db.Column(db.String)
    location_type = db.Column(db.String)

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)


class Employment(db.Model):
    __tablename__ = 'employments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    minimum_pay = db.Column(db.Integer)
    maximum_pay = db.Column(db.Integer)
    minimum_duration = db.Column(db.String)
    currencies = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)

class Contractor(db.Model):
    __tablename__ = 'contractors'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    start_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    minimum_rate = db.Column(db.Integer)
    maximum_rate = db.Column(db.Integer)
    minimum_duration = db.Column(db.String)
    currencies = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)


class Workplace(db.Model):    
###Places of work to be listed here
   __tablename__ = 'workplaces'
    name = StringField(' Name of the organization')
    description = db.Column(db.String)
    role = db.Column(db.String)
    role_description = db.Column(db.String)
    start_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    currently = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)

class School(db.Model): 
###Schools to be listed here
   __tablename__ = 'schools'
    name = db.Column(db.String)
    description = db.Column(db.String)
    grading = db.Column(db.String)
    start_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    currently = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
