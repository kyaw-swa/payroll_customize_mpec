from odoo import models,fields,api

class Leaves(models.Model):
    _name = 'payroll.leaves'
    _description = 'payroll.leaves'

    # Absence and Leave Money
    currency_id = fields.Many2one("res.currency")
    late_than_0815 = fields.Monetary('Late Than 08:15','currency_id')
    late_than_0830 = fields.Monetary('Late Than 08:30','currency_id')
    medical_leave = fields.Monetary('Medical Leave','currency_id')
    unauthorized_leave = fields.Monetary('Unauthorized Leave','currency_id')
    unauthorized_permission = fields.Monetary('Unauthorized Permission','currency_id')
    total_absence = fields.Monetary('Total Absence','currency_id', compute='_compute_total_absence')
    
    @api.depends('late_than_0815', 'late_than_0830', 'medical_leave', 'unauthorized_leave', 'unauthorized_permission')
    def _compute_total_absence(self):
        for employee in self:
            total_absence = employee.late_than_0815 + employee.late_than_0830 + employee.medical_leave + employee.unauthorized_leave + employee.unauthorized_permission
            employee.total_absence = total_absence