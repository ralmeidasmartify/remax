from odoo import fields, models


class CambiodeFacturas(models.Model):
    _name = "facturas.cambiar"
    _description = " Este objeto adhiere la accion de ventana para poder cambiar facturas de compañia"


# name = fields.Char(string='Name')   
# facturas_de_cambio = fields.many2many('account.move', string= 'Facturas que se van cambiar')
# destination_company = fields.Selection([
#     ('company1', 'Senado de la Republica'),
#     ('company2', 'Odebrech'),
#     ('company2', 'Ministerio Publico'),
# ], string='Compañia Destino')
