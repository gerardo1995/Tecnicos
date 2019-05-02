
# -*- coding: utf-8 -*-
from odoo import fields, models

class Usuarios(models.Model):
    _name = 'technician.usuarios'
    _description = 'tablad de usuarios'
    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email', required=True)
    password= fields.Char(string='Contraseña')
    phone= fields.Char(string='Telefono')
    rol_id= fields.one2Many(comodel_name='technician.rol', string='Userrol')
    dept_id=fields.one2Many(comodel_name='technician.dept', string='Department')
    task_ids=fields.Many2Many(comodel_name="technician_task", relation="technician_x_task", 
                              column1="user_id", column2="task_id", string="Tareas")