from odoo import models,fields
    
class Persona(models.Model):
    _name = "tareas.persona"

    first_name = fields.Char("Nombre")
    last_name = fields.Char("Apellido")
    phone = fields.Char("Telefono")
    email = fields.Char("Correo")
    img = fields.Binary("Perfil")
    tarea_ids = fields.Many2many("tareas.tarea", string ="Tareas asignadas")

class Tarea(models.Model):
    _name = "tareas.tarea"
    _rec_name ="tname"

    tname = fields.Char("Nombre de la tarea")
    tdesc = fields.Char("Descripcion de la tarea")
    tfecha_inicio = fields.Datetime("Fecha de inicio")
    tfecha_final = fields.Datetime("Fecha de final")
    timg = fields.Binary("Imagen tarea")
    testado = fields.Selection(selection=[("pendiente","Pendiente"),("terminado","Terminado"),("proceso","En Proceso")], string ="Estado")
    persona_ids = fields.Many2many("tareas.persona", string ="Personas asignidas a la tarea")

