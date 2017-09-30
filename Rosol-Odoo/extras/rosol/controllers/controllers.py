# -*- coding: utf-8 -*-
from odoo import http

# class Rosol(http.Controller):
#     @http.route('/rosol/rosol/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rosol/rosol/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rosol.listing', {
#             'root': '/rosol/rosol',
#             'objects': http.request.env['rosol.rosol'].search([]),
#         })

#     @http.route('/rosol/rosol/objects/<model("rosol.rosol"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rosol.object', {
#             'object': obj
#         })