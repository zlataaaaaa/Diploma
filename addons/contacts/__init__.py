from odoo import models, fields, api


class Contact(models.Model):
    _name = 'my_module.contact'

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    phone = fields.Char(string='Phone')

    @api.model
    def create(self, vals):
        contact = super(Contact, self).create(vals)
        # Дополнительные действия при создании контакта
        return contact
