from odoo import api, fields, models

class School(models.Model):
    _name = 'school.student'

    name = fields.Many2one(comodel_name='res.partner', string='Student')
    class_id = fields.Integer(string='Class')
    division = fields.Char(string='Division')
    _inherit = 'school.student'

    @api.model
    def create(self, vals):
        # Ваша логика создания записи
        return super(School, self).create(vals)