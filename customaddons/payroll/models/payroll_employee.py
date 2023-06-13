from odoo import models, fields, api

class Employee(models.Model):
    _name = 'payroll.employee'
    _description = 'payroll.employee'
    
    employee_name = fields.Char('Employee Name')
    job_position = fields.Selection([        
                                 
        ('mr','MR'),
        ('dm','DM'),
        ('am','AM'),
        ('senior_engineer','Senior Engineer'),
        ('senior_spv_engineer','Senior SPV / Engineer'),
        ('supervisor_ae','Supervisor / AE'),
        ('Asst_supervisor_sae','Asst Supervisor / SAE'),
        ('senior_techincian_1','Senior Technician-1'),
        ('senior_techincian_2','Senior Technician-2'),
        ('techincian_grade_1','Technician Grade-1'),
        ('techincian_grade_2','Technician Grade-2'),
        ('techincian_grade_3','Technician Grade-3'),
        ('techincian_grade_4','Technician Grade-4'),
        ('techincian_grade_5','Technician Grade-5'),
        ('techincian_grade_6','Technician Grade-6'),
        
        
    ],'Job Position')
    
    # Basic Salary
    currency_id = fields.Many2one("res.currency")
    basic_salary = fields.Monetary('Basic Salary','currency_id')
    total_basic_salary = fields.Monetary('Total Basic Salary','currency_id',compute='_compute_total_basic_salary')
    basic_salary_80 = fields.Monetary('Basic Salary(80%)','currency_id',compute='_compute_basic_salary_80')
    additional_salary_20 = fields.Monetary('Additional Salary(20%) + 10000','currency_id',compute='_compute_additional_salary_20')
    
    attendance_bonus = fields.Monetary('Attendance Bonus','currency_id', compute='_compute_attendance_bonus')
    overtime_hours = fields.Float('Overtime Hours')
    overtime_days = fields.Float('Overtime Days',)
    overtime_fee = fields.Monetary('Overtime Fee','currency_id', compute='_compute_overtime_fee')
    overtime_meal_allowance = fields.Monetary('Overtime Meal Allowance','currency_id')
    scholarship = fields.Monetary('Scholarship','currency_id')
    house_rent = fields.Monetary('House Rent','currency_id')
    phone_billing = fields.Monetary('Phone Billing','currency_id')
    yearly_increment = fields.Monetary('Yearly Increment','currency_id')
    total_salary = fields.Monetary('Total Salary','currency_id', compute='_compute_total_salary')
    
    # Advance WIthdrawal
    advance_1 = fields.Monetary('Advance 1','currency_id')
    advance_2 = fields.Monetary('Advance 2','currency_id')
    advance_3 = fields.Monetary('Advance 3','currency_id')
    advance_4 = fields.Monetary('Advance 4','currency_id')
    advance_5 = fields.Monetary('Advance 5','currency_id')
    total_advance = fields.Monetary('Total Advance','currency_id', compute='_compute_total_advance')
    
    # Absence and Leave Money
    late_than_0815 = fields.Monetary('Late Than 08:15','currency_id')
    late_than_0830 = fields.Monetary('Late Than 08:30','currency_id')
    medical_leave = fields.Monetary('Medical Leave','currency_id')
    unauthorized_leave = fields.Monetary('Unauthorized Leave','currency_id')
    unauthorized_permission = fields.Monetary('Unauthorized Permission','currency_id')
    total_absence = fields.Monetary('Total Absence','currency_id', compute='_compute_total_absence')
    
    # Total Payment
    total_payment = fields.Monetary('Total Payment','currency_id', compute='_compute_total_payment')

    

    @api.depends('basic_salary')
    def _compute_total_basic_salary(self):
        for employee in self:
            employee.total_basic_salary = employee.basic_salary + 10000
    def _compute_basic_salary_80(self):
        for employee in self:
            employee.basic_salary_80 = employee.basic_salary * 0.8
    def _compute_additional_salary_20(self):
        for employee in self:
            employee.additional_salary_20 = employee.basic_salary * 0.2 + 10000
    def _compute_attendance_bonus(self):
        for employee in self:
            employee.attendance_bonus = employee.basic_salary * 0.1

    @api.depends('overtime_hours', 'overtime_days')
    def _compute_overtime_fee(self):
        for employee in self:
            overtime_fee = ((employee.overtime_hours/8) + employee.overtime_days) * employee.basic_salary * 0.05
            employee.overtime_fee = overtime_fee

    @api.depends('basic_salary', 'attendance_bonus', 'overtime_fee', 'overtime_meal_allowance', 'scholarship', 'house_rent', 'phone_billing', 'yearly_increment')
    def _compute_total_salary(self):
        for employee in self:
            total_salary = employee.basic_salary + employee.attendance_bonus + employee.overtime_fee + employee.overtime_meal_allowance + employee.scholarship + employee.house_rent - employee.phone_billing + employee.yearly_increment
            employee.total_salary = total_salary
            
    @api.depends('advance_1', 'advance_2', 'advance_3', 'advance_4', 'advance_5')
    def _compute_total_advance(self):
        for employee in self:
            total_advance = employee.advance_1 + employee.advance_2 + employee.advance_3 + employee.advance_4 + employee.advance_5
            employee.total_advance = total_advance
            
    @api.depends('late_than_0815', 'late_than_0830', 'medical_leave', 'unauthorized_leave', 'unauthorized_permission')
    def _compute_total_absence(self):
        for employee in self:
            total_absence = employee.late_than_0815 + employee.late_than_0830 + employee.medical_leave + employee.unauthorized_leave + employee.unauthorized_permission
            employee.total_absence = total_absence

    @api.depends('total_salary', 'total_advance', 'total_absence')
    def _compute_total_payment(self):
        for employee in self:
            total_payment = employee.total_salary - employee.total_advance - employee.total_absence
            employee.total_payment = total_payment
            
    @api.onchange('job_position')
    def _onchange_position(self):
        salary_dict = {
            'mr': 340000,
            'dm': 320000,
            'am': 300000 ,
            'senior_engineer': 280000 ,
            'senior_spv_engineer': 265000,
            'supervisor_ae': 250000,
            'Asst_supervisor_sae': 235000,
            'senior_techincian_1': 220000,
            'senior_techincian_2': 210000,
            'techincian_grade_1': 200000,
            'techincian_grade_2': 190000,
            'techincian_grade_3': 180000,
            'techincian_grade_4': 170000 ,
            'techincian_grade_5': 160000,
            'techincian_grade_6': 150000,
              
        }
        self.basic_salary = salary_dict.get(self.job_position, 0)