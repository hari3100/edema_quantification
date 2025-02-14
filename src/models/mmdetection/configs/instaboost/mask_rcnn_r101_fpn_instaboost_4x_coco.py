_base_ = './mask_rcnn_r50_fpn_instaboost_4x_coco.py'
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='torchvision://resnet101',
        ),
    ),
)
