# -*- coding: utf-8 -*-
from odoo import fields, models

class Productos(models.Model):

    _name = 'productos'
    name = fields.Char(string='Nombre', required=True)
    description= fields.Char(string='Descripcion')
    date_of_admission = fields.Date(string='Fecha de ingreso')
    cuantity= fields.Integer(string='Cantidad')

class Proveedor(models.Model):
    _name = 'proveedor'

    _id = fields.Many2one(comodel_name='medic_hn.patient', string='Paciente')

class Vendedor(models.Model):
    _inherit = ['sale.order']

    patient_id = fields.Many2one(comodel_name='medic_hn.patient', string='Paciente')


class Categoria(models.Model):
    _inherit = ['sale.order']

    patient_id = fields.Many2one(comodel_name='medic_hn.patient', string='Paciente')
    
 
    
    