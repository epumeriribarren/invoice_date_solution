from odoo import api, exceptions, fields, models, _
from odoo.exceptions import UserError

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def action_date_assign(self):
        for inv in self:
            # Here the onchange will automatically write to the database
            if not inv.date_invoice:
                raise UserError(_('Debes seleccionar una fecha para la factura antes de validarla.'))
            inv._onchange_payment_term_date_invoice()
        return True