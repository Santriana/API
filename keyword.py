from marshmallow import Schema, fields

class input(Schema):
    mid_score = fields.Int(required=True)
    overall_mid_weight = fields.Int(required=True)
    mid_weight = fields.Int(required=True)
    final_score = fields.Int(required=True)
    overall_final_weight = fields.Int(required=True)
    final_weight = fields.Int(required=True)