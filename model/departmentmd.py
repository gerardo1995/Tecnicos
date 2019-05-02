
# -*- coding: utf-8 -*-
from odoo import fields, models

class Departamento(models.Model):
    _name ='technician.departamento'
    _description = 'tablad de departamentos'
    name=fields.Char(string='Departamento')
