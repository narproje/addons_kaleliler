import base64
from odoo import models, fields, api
# import zint

class BarcodeGenerator(models.Model):
    _name = 'barcode.generator'
    _description = 'Barcode Generator using Zint'

    name = fields.Char('Name', required=True)
    barcode_data = fields.Binary('Barcode', attachment=True)

    @api.model
    def create_barcode(self, data, file_type='PNG'):
        barcode = zint.Barcode()
        barcode.code = data
        barcode.text = data
        barcode.type = zint.BARCODE_CODE128
        barcode.render(file_type)

        barcode_image = barcode.dump()
        return base64.b64encode(barcode_image).decode('utf-8')

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    barcode_image = fields.Binary('Barcode Image', attachment=True)

    def generate_product_barcode(self):
        for record in self:
            barcode_gen = self.env['barcode.generator']
            barcode_image_data = barcode_gen.create_barcode(record.product_id.default_code)
            record.barcode_image = barcode_image_data

    
    def action_print_label(self):
        obj_report_action = self.env['ir.actions.report'].sudo().search([('name','=', 'Ürün Çıktı')])
        report_action =obj_report_action.report_action(self.product_id.product_tmpl_id,config=False)
        return report_action


    
