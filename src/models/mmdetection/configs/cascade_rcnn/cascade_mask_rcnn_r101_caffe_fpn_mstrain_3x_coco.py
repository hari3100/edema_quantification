_base_ = './cascade_mask_rcnn_r50_caffe_fpn_mstrain_3x_coco.py'
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='open-mmlab://detectron2/resnet101_caffe',
        ),
    ),
)
