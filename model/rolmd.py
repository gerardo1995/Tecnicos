
# -*- coding: utf-8 -*-
from odoo import fields, models

class Rol(models.Model):
    _name = 'technician.rol'
    _description = 'tablad de roles'
    name= fields.Char(string='Rol')