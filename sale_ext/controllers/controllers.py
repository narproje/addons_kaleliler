# -*- coding: utf-8 -*-
# from odoo import http


# class SaleExt(http.Controller):
#     @http.route('/sale_ext/sale_ext', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_ext/sale_ext/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_ext.listing', {
#             'root': '/sale_ext/sale_ext',
#             'objects': http.request.env['sale_ext.sale_ext'].search([]),
#         })

#     @http.route('/sale_ext/sale_ext/objects/<model("sale_ext.sale_ext"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_ext.object', {
#             'object': obj
#         })
