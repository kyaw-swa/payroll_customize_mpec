from odoo import fields,models

class CurriculumVitaeSimple(models.Model):
    _name = 'curriculum.vitae.simple'
    _description = 'Curriculum Vitae Simple Format'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    active = fields.Boolean(string='Active',default=True)
    
    cv_image = fields.Binary(string='CV Image', attachment=True)
    job_type = fields.Selection([
        ('customer_service','Customer Service'),
        ('system_analyser','System Analyser'),
        ('software_developer','Software Developer'),
        ('web_developer','Web Developer'),
        ('quality_assurance','Quality Assurance')
    ],string='Job Type', default='software_developer',required=True)
    
    name = fields.Char(string='Name')
    nrc = fields.Char(string='NRC')
    date_of_birth = fields.Date(string='Date of Birth')
    place_of_birth = fields.Char(string='Place of Birth')
    nationality = fields.Char(string='Nationality')
    
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
        ],string='Gender',default='male',required=True)
    qualification = fields.Char(string='Qualification')
    hobby = fields.Char(string='Hobby')
    address = fields.Char(string='Address')
    permanent_address = fields.Char(string='Permanent Address')
    
    email = fields.Char(string='Email')
    facebook = fields.Char(string='Facebook')
    phone = fields.Char(string='Phone')
    field_of_interest = fields.Char(string='Field of Interest')
    working_experience = fields.Char(string='Working Experience')