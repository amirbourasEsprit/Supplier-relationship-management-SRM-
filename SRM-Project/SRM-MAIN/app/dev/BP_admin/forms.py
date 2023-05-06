from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, HiddenField, SelectField, RadioField, DateField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flask_babel import gettext, lazy_gettext
from dev.models import *
from dev import db
from datetime import datetime

class Select2MultipleField(SelectMultipleField):

    def pre_validate(self, form):
        # Prevent "not a valid choice" error
        pass

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = "".join(valuelist)
        else:
            self.data = ""


class Update_Profile_Form(FlaskForm):

	firstName= StringField( lazy_gettext('Prénom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Prénom')})
	lastName= StringField( lazy_gettext('Nom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Nom')})
	email= StringField( lazy_gettext('Email'), validators=[DataRequired(), Email()], render_kw={"placeholder" : lazy_gettext(u'Email')})
	phone= StringField( lazy_gettext('Numéro du téléphone'), render_kw={"placeholder" : lazy_gettext(u'Numéro du téléphone')})
	submit= SubmitField(lazy_gettext(u"  Valider  "))

	def validate_phone(self, phone):
		if not(phone.data.isnumeric()) or len(phone.data)!=8:
			raise ValidationError('vérifiez votre numéro de téléphone')

class Update_Password_Form(FlaskForm):

	old_password=PasswordField(lazy_gettext('Mot de passe actuel'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Entrez votre mot de passe actuel')})
	new_password=PasswordField(lazy_gettext('Nouveau mot de passe'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Entrez votre nouveau mot de passe')})
	confirm_password=PasswordField(lazy_gettext('Confirmer mot de passe'), validators=[DataRequired(), EqualTo('new_password', message='vérifiez le nouveau mot de passe')], render_kw={"placeholder" : lazy_gettext(u'Confirmer votre nouveau mot de passe')})
	submit= SubmitField(lazy_gettext(u"Valider"))

class Add_Sysuser_Form(FlaskForm):
	companies= Company.query.all()
	sites= Site.query.all()
	roles= Role.query.all()

	firstName= StringField( lazy_gettext('Prénom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Prénom')})
	lastName= StringField( lazy_gettext('Nom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Nom')})
	email= StringField( lazy_gettext('Email'), validators=[DataRequired(), Email()], render_kw={"placeholder" : lazy_gettext(u'Email')})
	company = SelectField( lazy_gettext('Choisir une Entité juridique :'), validators=[DataRequired()],  choices = [(company.id, company.name) for company in companies])
	site = SelectField( lazy_gettext('Choisir un site :'), validators=[DataRequired()],  choices = [(site.id, site.name) for site in sites])
	role = Select2MultipleField( lazy_gettext('Choisir les roles :'), choices = [(role.id, role.name) for role in roles])
	submit= SubmitField(lazy_gettext(u"  Valider  "))

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email déjà utilisé')

class Update_Sysuser_Form(FlaskForm):
	companies= Company.query.all()
	sites= Site.query.all()
	roles= Role.query.all()

	uniqueIdentifier= StringField( lazy_gettext('Identifiant Unique'), render_kw={"placeholder" : lazy_gettext(u'Identifiant Unique')})
	firstName= StringField( lazy_gettext('Prénom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Prénom')})
	lastName= StringField( lazy_gettext('Nom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Nom')})
	email= StringField( lazy_gettext('Email'), validators=[DataRequired(), Email()], render_kw={"placeholder" : lazy_gettext(u'Email')})
	company = SelectField( lazy_gettext('Choisir une Entité juridique :'), validators=[DataRequired()],  choices = [(company.id, company.name) for company in companies])
	site = SelectField( lazy_gettext('Choisir un site :'), validators=[DataRequired()],  choices = [(site.id, site.name) for site in sites])
	role = Select2MultipleField( lazy_gettext('Choisir les roles :'), choices = [(role.id, role.name) for role in roles])
	submit= SubmitField(lazy_gettext(u"  Valider  "))

class Add_Suppuser_Form(FlaskForm):
	suppliers= Supplier.query.all()
	roles= Role.query.filter(Role.id>1).all()

	firstName= StringField( lazy_gettext('Prénom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Prénom')})
	lastName= StringField( lazy_gettext('Nom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Nom')})
	email= StringField( lazy_gettext('Email'), validators=[DataRequired(), Email()], render_kw={"placeholder" : lazy_gettext(u'Email')})
	supplier = SelectField( lazy_gettext('Choisir un fournisseur :'), validators=[DataRequired()],  choices = [(supplier.id, supplier.name) for supplier in suppliers])
	role = Select2MultipleField( lazy_gettext('Choisir les roles :'), choices = [(role.id, role.name) for role in roles])
	submit= SubmitField(lazy_gettext(u"  Valider  "))

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email déjà utilisé')

class Update_Suppuser_Form(FlaskForm):
	roles= Role.query.filter(Role.id>1).all()

	uniqueIdentifier= StringField( lazy_gettext('Identifiant Unique'), render_kw={"placeholder" : lazy_gettext(u'Identifiant Unique')})
	firstName= StringField( lazy_gettext('Prénom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Prénom')})
	lastName= StringField( lazy_gettext('Nom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Nom')})
	email= StringField( lazy_gettext('Email'), validators=[DataRequired(), Email()], render_kw={"placeholder" : lazy_gettext(u'Email')})
	role = Select2MultipleField( lazy_gettext('Choisir les roles :'), choices = [(role.id, role.name) for role in roles])
	submit= SubmitField(lazy_gettext(u"  Valider  "))

class Add_Company_Form(FlaskForm):

	name= StringField( lazy_gettext('Nom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Nom')})
	taxRegisration= StringField( lazy_gettext('Matricule Fiscal'), render_kw={"placeholder" : lazy_gettext(u'Matricule Fiscal')})
	phone= StringField( lazy_gettext('Numéro du téléphone'), render_kw={"placeholder" : lazy_gettext(u'Numéro du téléphone')})
	fax= StringField( lazy_gettext('Numéro du fax'), render_kw={"placeholder" : lazy_gettext(u'Numéro du fax')})
	adresse= StringField( lazy_gettext('Adresse'), render_kw={"placeholder" : lazy_gettext(u'Adresse')})
	city= StringField( lazy_gettext('Ville'), render_kw={"placeholder" : lazy_gettext(u'Ville')})
	country= StringField( lazy_gettext('Pays'), render_kw={"placeholder" : lazy_gettext(u'Pays')})
	submit= SubmitField(lazy_gettext(u"  Valider  "))
	
	def validate_tax(self, taxRegisration):
		company = Company.query.filter_by(taxRegisration=taxRegisration.data).first()
		if company:
			raise ValidationError('Matricule fiscale déjà utilisé')

	def validate_phone(self, phone):
		if not(phone.data.isnumeric()) or len(phone.data)!=8:
			raise ValidationError('vérifiez le numéro de téléphone')

	def validate_fax(self, fax):
		if not(fax.data.isnumeric()) or len(fax.data)!=8:
			raise ValidationError('vérifiez le numéro du fax')

class Update_Company_Form(FlaskForm):

	uniqueIdentifier= StringField( lazy_gettext('Identifiant Unique'), render_kw={"placeholder" : lazy_gettext(u'Identifiant Unique')})
	name= StringField( lazy_gettext('Nom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Nom')})
	taxRegisration= StringField( lazy_gettext('Matricule Fiscal'), render_kw={"placeholder" : lazy_gettext(u'Matricule Fiscal')})
	phone= StringField( lazy_gettext('Numéro du téléphone'), render_kw={"placeholder" : lazy_gettext(u'Numéro du téléphone')})
	fax= StringField( lazy_gettext('Numéro du fax'), render_kw={"placeholder" : lazy_gettext(u'Numéro du fax')})
	adresse= StringField( lazy_gettext('Adresse'), render_kw={"placeholder" : lazy_gettext(u'Adresse')})
	city= StringField( lazy_gettext('Ville'), render_kw={"placeholder" : lazy_gettext(u'Ville')})
	country= StringField( lazy_gettext('Pays'), render_kw={"placeholder" : lazy_gettext(u'Pays')})
	submit= SubmitField(lazy_gettext(u"  Valider  "))

	def validate_phone(self, phone):
		if not(phone.data.isnumeric()) or len(phone.data)!=8:
			raise ValidationError('vérifiez le numéro de téléphone')

	def validate_fax(self, fax):
		if not(fax.data.isnumeric()) or len(fax.data)!=8:
			raise ValidationError('vérifiez le numéro du fax')

class Update_Logo_Form(FlaskForm):

	file=FileField(lazy_gettext('Logo'), validators=[FileAllowed(['jpeg', 'jpg', 'png', 'gif'])], render_kw={"placeholder" : lazy_gettext(u'Logo')})
	submit= SubmitField(lazy_gettext(u"Valider"))

class Add_Site_Form(FlaskForm):

	name= StringField( lazy_gettext('Nom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Nom')})
	phone= StringField( lazy_gettext('Numéro du téléphone'), render_kw={"placeholder" : lazy_gettext(u'Numéro du téléphone')})
	fax= StringField( lazy_gettext('Numéro du fax'), render_kw={"placeholder" : lazy_gettext(u'Numéro du fax')})
	adresse= StringField( lazy_gettext('Adresse'), render_kw={"placeholder" : lazy_gettext(u'Adresse')})
	city= StringField( lazy_gettext('Ville'), render_kw={"placeholder" : lazy_gettext(u'Ville')})
	country= StringField( lazy_gettext('Pays'), render_kw={"placeholder" : lazy_gettext(u'Pays')})
	submit= SubmitField(lazy_gettext(u"  Valider  "))

	def validate_phone(self, phone):
		if not(phone.data.isnumeric()) or len(phone.data)!=8:
			raise ValidationError('vérifiez le numéro de téléphone')

	def validate_fax(self, fax):
		if not(fax.data.isnumeric()) or len(fax.data)!=8:
			raise ValidationError('vérifiez le numéro du fax')

class Update_Site_Form(FlaskForm):

	uniqueIdentifier= StringField( lazy_gettext('Identifiant Unique'), render_kw={"placeholder" : lazy_gettext(u'Identifiant Unique')})
	name= StringField( lazy_gettext('Nom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Nom')})
	phone= StringField( lazy_gettext('Numéro du téléphone'), render_kw={"placeholder" : lazy_gettext(u'Numéro du téléphone')})
	fax= StringField( lazy_gettext('Numéro du fax'), render_kw={"placeholder" : lazy_gettext(u'Numéro du fax')})
	adresse= StringField( lazy_gettext('Adresse'), render_kw={"placeholder" : lazy_gettext(u'Adresse')})
	city= StringField( lazy_gettext('Ville'), render_kw={"placeholder" : lazy_gettext(u'Ville')})
	country= StringField( lazy_gettext('Pays'), render_kw={"placeholder" : lazy_gettext(u'Pays')})
	submit= SubmitField(lazy_gettext(u"  Valider  "))

	def validate_phone(self, phone):
		if not(phone.data.isnumeric()) or len(phone.data)!=8:
			raise ValidationError('vérifiez le numéro de téléphone')

	def validate_fax(self, fax):
		if not(fax.data.isnumeric()) or len(fax.data)!=8:
			raise ValidationError('vérifiez le numéro du fax')

class Add_Excel_Form(FlaskForm):

	file=FileField(lazy_gettext('Fichier source'), validators=[FileRequired(), FileAllowed(['xls', 'xlsx', 'csv'])], render_kw={"placeholder" : lazy_gettext(u'Ficheir source')})
	submit= SubmitField(lazy_gettext(u"Valider"))

class Add_Charge_Form(FlaskForm):
	code = StringField('Code Frais', validators=[
		DataRequired(message='Ce champs est obligatoire!'),
        Length(min=2,max=30,message='Le nom doit être entre 2 et 30 caractères!')
    ])
	# if units are manually added by user, the choices list should be replaced to query the list of units
	# for now there are defined list
	unit = SelectField('Unité',  choices = [(' ',' '),('Heure','Heure'),('KM','KM')])
	description = TextAreaField('Description du frais')
	submit = SubmitField('  Valider  ')
	def validate_code(self, code):
		cost = CostType.query.filter_by(code=code.data).first()
		if cost:
			raise ValidationError('Ce code frais est déjà utilisé !')
	

class Update_Charge_Form(FlaskForm):
	code = StringField('Code Frais', validators=[
		DataRequired(message='Ce champs est obligatoire!'),
        Length(min=2,max=30,message='Le nom doit être entre 2 et 30 caractères !')
    ])
	# if units are manually added by user, the choices list should be replaced to query the list of units
	# for now there are defined list
	unit = SelectField('Unité',  choices = [(' ',' '),('Heure','Heure'),('KM','KM')])
	description = TextAreaField('Description du frais')
	submit = SubmitField('  Valider  ')	

def numeric_check(form,field):
		if not(field.data.isnumeric()):
			raise ValidationError('Ce champs doit être numérique!')

class Add_typeCertificate_Form(FlaskForm):

	name= StringField( lazy_gettext('Nom'), validators=[DataRequired()], render_kw={"placeholder" : lazy_gettext(u'Nom')})
	description= TextAreaField( lazy_gettext('Description'), render_kw={"placeholder" : lazy_gettext(u'Description')})
	submit= SubmitField(lazy_gettext(u"  Valider  "))