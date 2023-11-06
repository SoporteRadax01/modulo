from odoo import models, fields, api,_
from odoo.exceptions import Warning,ValidationError
from odoo.exceptions import UserError
class alerta(models.Model):
    _inherit = 'stock.move'


    nuevo1 = fields.Float(string="nuevo")


    def button_confirm(self):
        for move in self:
            if move.nuevo1 < 0:
                raise UserError(_("No se puede confirmar el movimiento, la cantidad de un producto no es suficiente. Por favor, revise los componentes."))
        return  self.write({'state':'confirmed'})



