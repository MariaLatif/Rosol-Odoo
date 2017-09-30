# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rosol(models.Model):
    _name = 'rosol.rosol'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    ssn = fields.Char(string='SSN')
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Html(string='Description')

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100