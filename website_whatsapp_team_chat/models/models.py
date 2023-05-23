# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WhatsAppChatTeam(models.Model):
    _name = "whats.app.chat.team"

    name = fields.Char('Name')
    whatsapp_chat_title = fields.Char(string="WhatsApp Chat Title", default="Contact Us By WhatsApp")
    team_members_ids = fields.Many2many('res.partner', string='Team Members')


class ResPartner(models.Model):
    _inherit = "res.partner"

    time = fields.Char('Time')
    department = fields.Char('Department')


class ResCompany(models.Model):
    _inherit = "res.company"

    team_id = fields.Many2one('whats.app.chat.team', string='WhatsApp Support Team')
