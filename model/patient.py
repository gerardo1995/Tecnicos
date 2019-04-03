# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models, _

class Patient(models.Model):

    _name = 'medic_hn.patient'


    name = fields.Char(string='Nombre', required=True)
    identidad = fields.Char(string='Identidad')

    gender = fields.Selection(string='Género', 
        selection=[('m', 'Másculino'), ('f', 'Feménino'),])
    
    date_borth = fields.Date(string='Fecha de Nacimiento')


    
class SaleOrder(models.Model):
    _inherit = ['sale.order']

    patient_id = fields.Many2one(comodel_name='medic_hn.patient', string='Paciente')
    
 
    
    