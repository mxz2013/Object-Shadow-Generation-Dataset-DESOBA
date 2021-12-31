
#!/bin/bash
batchs=1
GPU=0
lr=0.0002
loadSize=256
fineSize=256
L1=100
model=Pix2pix
G='RESNEXT18'
ngf=32


L_light=0
L_para=1
L_shadowrecons=10
L_imagerecons=10
L_GAN=1

#####network design
DISPLAY_PORT=8002
D='pixel'
lr_D=0.0002
Residual=0



model_name=Pix2pix


#####datset selected
datasetmode=shadowparam



NAME="${model_name}_G${G}_C${ngf}_D${D}_lrD${lr_D}"
FinetuneModel='${NAME}latest'




#aaai 2021
checkpoint='../../TrainedModels/New_Pix2pix_TrainedModel/'



dataroot='../../DESOBA_DATASET/'
shadowimage_path=${dataroot}'/ShadowImage'
shadowfree_path=${dataroot}'/DeshadowedImage'
new_mask_path=${dataroot}'/shadownewmask'
param_path=${dataroot}'/SOBA_params'
bg_shadow_path=${dataroot}'/ShadowMask'
bg_instance_path=${dataroot}'/InstanceMask'



OTHER="--save_epoch_freq 1 --display_freq 100 --niter 500 --niter_decay 2000  --no_crop --no_flip --no_rotate  "

CMD="python ../train.py --loadSize ${loadSize} \
    --name ${NAME} \
    --checkpoints_dir ${checkpoint} \
    --fineSize $fineSize --model $model\
    --batch_size $batchs --display_port ${DISPLAY_PORT}
    --display_server http://localhost
    --phase train  --gpu_ids ${GPU} --lr ${lr} \
    --dataset_mode $datasetmode\

    --norm instance\
    --dataroot  ${dataroot}\
    --param_path $param_path\
    --shadowimg_path $shadowimage_path\
    --shadowfree_path $shadowfree_path\
    --bg_shadow_path $bg_shadow_path\
    --bg_instance_path $bg_instance_path\
    --new_mask_path $new_mask_path\


    --lambda_M1 $L_shadowrecons --lambda_I1 $L_imagerecons --lambda_GAN $L_GAN 
    --netG $G\
    --ngf $ngf
    --netD $D
    --lr_D $lr_D
    --residual $Residual



    $OTHER
"
echo $CMD
eval $CMD


