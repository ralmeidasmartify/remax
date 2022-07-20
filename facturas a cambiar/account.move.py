from odoo import fields, models


class CambiodeFacturas(models.Model):
    _inherit = 'cambio.facturas'
    _description = 'Cambiar facturas de empresa'

name = fields.Char(string='Name')   
facturas_de_cambio = fields.many2many('account.move', string= 'Facturas que se van cambiar')
