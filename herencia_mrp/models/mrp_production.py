from odoo import models, fields, api,_
from odoo.exceptions import Warning,ValidationError
from odoo.exceptions import UserError
class alerta(models.Model):
    _inherit = 'mrp.production'




    def action_confirm3(self):
        for production in self:
            # Llama al método personalizado en stock.move que realiza la validación y confirmación.
            production.move_raw_ids.button_confirm()

    def action_confirm(self):
        self.action_confirm3()
        result = super(alerta, self).action_confirm()
        return result
