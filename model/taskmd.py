
# -*- coding: utf-8 -*-

from odoo import fields, models

class Task(models.Model):
    _name ='technician.tarea'
    _description = 'tablad de tareas'
    name=fields.Char(string='Tarea')
    
