_base_ = '../ssd/ssd512_coco.py'

model = dict(
    bbox_head=dict(type='PISASSDHead'),
    train_cfg=dict(isr=dict(k=2.0, bias=0.0), carl=dict(k=1.0, bias=0.2)),
)

optimizer_config = dict(
    _delete_=True,
    grad_clip=dict(max_norm=35, norm_type=2),
)
