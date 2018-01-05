from __future__ import print_function
import os

#  epochs = 100
epochs = 60 
vgg_weight = '/home/cfchen/pytorch_models/vgg_conv.pth'
model_version = 1
norm = 'IN'
layers = [0, 0, 1, 1, 1]
#  layers = [0, 0, 0, 0, 1]
weight = [1e0, 1e-1, 1e-4]  # mse loss, feature loss, tv loss
loss_func = 4
direction = "AtoB"
#  direction = "BtoA"
resume = 0
#  other = '_grayout'
other = '_coloraug-sizeaug'
#  other = '_coloraug'
#  train_data = './small_data'
#  train_data = '/data2/cfchen/pytorch-CycleGAN-and-pix2pix/datasets/edges2shoes/train'
#  train_data = '/data2/cfchen/pytorch-CycleGAN-and-pix2pix/datasets/cityscapes/train'
#  train_data = '/data2/cfchen/pytorch-CycleGAN-and-pix2pix/datasets/facades/train'
#  train_data = '/data2/cfchen/pytorch-CycleGAN-and-pix2pix/datasets/edges2handbags/train'
#  train_data = '/data2/cfchen/pytorch-CycleGAN-and-pix2pix/datasets/maps/train'
train_data = './face_sketch_data/CUHK_AR'
model_param = [
        '--train-data {}'.format(train_data),
        '--epochs {}'.format(epochs),
        '--vgg19-weight {}'.format(vgg_weight),
        '--model-version {}'.format(model_version),
        '--norm {}'.format(norm),
        '--weight {} {} {}'.format(*weight),
        '--loss-func {}'.format(loss_func),
        '--layers {} {} {} {} {}'.format(*layers),
        '--direction {}'.format(direction),
        '--other {}'.format(other),
        '--resume {}'.format(resume),
        ]

#  test_dir = '/data2/cfchen/pytorch-CycleGAN-and-pix2pix/datasets/cityscapes/val'
#  test_dir = './test/CUHK_student_test/photos' 
test_dir = './test/natural_face_test/photos' 
test_model = 'epochs-{:03d}.pth'.format(epochs - 1) 
#  test_model = 'epochs-{:03d}.pth'.format(1) 
result_root = './results/pix2pix-{}-{}-result-model{}-{}-layers{}-loss_{}-weight-{:.1e}-{:.1e}-{:.1e}{}'.format(
              test_dir.split('/')[-2], 
              direction, 
              model_version, norm, 
              "".join(map(str, layers)), loss_func, weight[0], weight[1], weight[2], other)


for root, dirs, names in os.walk(test_dir):
    for n in sorted(names):
        arguments = model_param + [
                    '--test-img ' + os.path.join(root, n),
                    '--test-model {}'.format(test_model),
                    '--result-root {}'.format(result_root)]
        #  print arguments
        os.system('python photo_to_photo_multiscale.py eval {}'.format(" ".join(arguments)))

