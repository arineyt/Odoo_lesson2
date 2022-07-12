# -*- coding: utf-8 -*-
from odoo import models, fields

class HospitalPatient(models.Model):
    """A class used to represent a Patient"""
    _name = 'hospital.patient'
    _description = "Hospital patient"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
