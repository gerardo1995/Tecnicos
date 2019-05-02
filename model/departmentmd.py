
# -*- coding: utf-8 -*-


class Departamento(models.Model):
    _name ='technician.departamento'
    _description = 'tablad de departamentos'
    name=fields.Char(string='Departamento')
