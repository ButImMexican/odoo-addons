# -*- coding: utf-8 -*-
# from odoo import http


# class Cambioor(http.Controller):
#     @http.route('/cambioor/cambioor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cambioor/cambioor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cambioor.listing', {
#             'root': '/cambioor/cambioor',
#             'objects': http.request.env['cambioor.cambioor'].search([]),
#         })

#     @http.route('/cambioor/cambioor/objects/<model("cambioor.cambioor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cambioor.object', {
#             'object': obj
#         })
