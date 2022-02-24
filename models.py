


#class UserName(db.Model):

	#user_id = db.Column(db.Integer, primary_key = True)
  
	#user_name = db.Column(db.String(150), nullable = False)
	
	#pred_v =  db.relationship('PredValues', backref='username', lazy = True)
	
#class PredValues(db.Model):
#	pred_v = db.Column(db.Integer,primary_key = False)
#	
#	user_id = db.Column(db.Integer, db.ForeignKey('username.user_id'), nullable = False)
