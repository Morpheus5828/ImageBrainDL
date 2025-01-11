
import torchvision
import functools
from brainscore_vision.model_helpers.activations.pytorch import PytorchWrapper
from brainscore_vision.model_helpers.activations.pytorch import load_preprocess_images


def load_alexnet():
    alexnet = torchvision.models.alexnet(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    alexnet = PytorchWrapper(identifier='alexnet', model=alexnet, preprocessing=preprocessing)
    alexnet.image_size = 224
    return alexnet


def load_alexnet_random():
    alexnet_random = torchvision.models.alexnet()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    alexnet_random = PytorchWrapper(identifier='alexnet_random', model=alexnet_random, preprocessing=preprocessing)
    alexnet_random.image_size = 224
    return alexnet_random


def load_squeezenet():
    squeezenet = torchvision.models.squeezenet1_1(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    squeezenet = PytorchWrapper(identifier='squeezenet', model=squeezenet, preprocessing=preprocessing)
    squeezenet.image_size = 224
    return squeezenet


def load_squeezenet_random():
    squeezenet_random = torchvision.models.squeezenet1_1()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    squeezenet_random = PytorchWrapper(identifier='squeezenet_random', model=squeezenet_random, preprocessing=preprocessing)
    squeezenet_random.image_size = 224
    return squeezenet_random


def load_vgg16():
    vgg = torchvision.models.vgg16(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    vgg = PytorchWrapper(identifier='vgg16', model=vgg, preprocessing=preprocessing)
    vgg.image_size = 224
    return vgg


def load_random_vgg16():
    vgg_random = torchvision.models.vgg16()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    vgg_random = PytorchWrapper(identifier='vgg16_random', model=vgg_random, preprocessing=preprocessing)
    vgg_random.image_size = 224
    return vgg_random


def load_vgg19():
    vgg = torchvision.models.vgg19(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    vgg = PytorchWrapper(identifier='vgg19', model=vgg, preprocessing=preprocessing)
    vgg.image_size = 224
    return vgg


def load_random_vgg19():
    vgg_random = torchvision.models.vgg19()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    vgg_random = PytorchWrapper(identifier='vgg19_random', model=vgg_random, preprocessing=preprocessing)
    vgg_random.image_size = 224
    return vgg_random


def load_googlenet():
    googlenet = torchvision.models.googlenet(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    googlenet = PytorchWrapper(identifier='googlenet', model=googlenet, preprocessing=preprocessing)
    googlenet.image_size = 224
    return googlenet


def load_random_googlenet():
    googlenet_random = torchvision.models.googlenet()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    googlenet_random = PytorchWrapper(identifier='googlenet_random', model=googlenet_random, preprocessing=preprocessing)
    googlenet_random.image_size = 224
    return googlenet_random


def load_inception():
    inception = torchvision.models.inception_v3(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    inception = PytorchWrapper(identifier='inception_v3', model=inception, preprocessing=preprocessing)
    inception.image_size = 224
    return inception


def load_random_inception():
    inception_random = torchvision.models.inception_v3()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    inception_random = PytorchWrapper(identifier='inception_v3_random', model=inception_random, preprocessing=preprocessing)
    inception_random.image_size = 224
    return inception_random


def load_mobilenet():
    mobilenet = torchvision.models.mobilenet_v3_small(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    mobilenet = PytorchWrapper(identifier='mobilenet', model=mobilenet, preprocessing=preprocessing)
    mobilenet.image_size = 224
    return mobilenet


def load_random_mobilenet():
    mobilenet_random = torchvision.models.mobilenet_v3_small()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    mobilenet_random = PytorchWrapper(identifier='mobilenet_random', model=mobilenet_random, preprocessing=preprocessing)
    mobilenet_random.image_size = 224
    return mobilenet_random


def load_resnet():
    resnet101 = torchvision.models.resnet101(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    resnet101 = PytorchWrapper(identifier='resnet101', model=resnet101, preprocessing=preprocessing)
    resnet101.image_size = 224
    return resnet101


def load_random_resnet():
    resnet101_random = torchvision.models.resnet101()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    resnet101_random = PytorchWrapper(identifier='resnet101_random', model=resnet101_random, preprocessing=preprocessing)
    resnet101_random.image_size = 224
    return resnet101_random


def load_densenet():
    densenet201 = torchvision.models.densenet201(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    densenet201 = PytorchWrapper(identifier='densenet201', model=densenet201, preprocessing=preprocessing)
    densenet201.image_size = 224
    return densenet201


def load_random_densenet201():
    densenet201_random = torchvision.models.densenet201()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    densenet201_random = PytorchWrapper(identifier='densenet201_random', model=densenet201_random, preprocessing=preprocessing)
    densenet201_random.image_size = 224
    return densenet201_random


def load_efficientnet_b7():
    efficientnet_b7 = torchvision.models.efficientnet_b7(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    efficientnet_b7 = PytorchWrapper(identifier='efficientnet_b7', model=efficientnet_b7, preprocessing=preprocessing)
    efficientnet_b7.image_size = 224
    return efficientnet_b7


def load_random_efficientnet_b7():
    efficientnet_b7_random = torchvision.models.efficientnet_b7()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    efficientnet_b7_random = PytorchWrapper(identifier='efficientnet_b7_random', model=efficientnet_b7_random, preprocessing=preprocessing)
    efficientnet_b7_random.image_size = 224
    return efficientnet_b7_random


def load_convnet():
    convnext_large = torchvision.models.convnext_large(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    convnext_large = PytorchWrapper(identifier='convnext_large', model=convnext_large, preprocessing=preprocessing)
    convnext_large.image_size = 224
    return convnext_large


def load_random_convnet_large():
    convnext_large_random = torchvision.models.convnext_large()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    convnext_large_random = PytorchWrapper(identifier='convnext_large_random', model=convnext_large_random, preprocessing=preprocessing)
    convnext_large_random.image_size = 224
    return convnext_large_random


def load_mnasnet1_3():
    mnasnet1_3 = torchvision.models.mnasnet1_3(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    mnasnet1_3 = PytorchWrapper(identifier='mnasnet1_3', model=mnasnet1_3, preprocessing=preprocessing)
    mnasnet1_3.image_size = 224
    return mnasnet1_3


def load_random_mnasnet1_3():
    mnasnet1_3_random = torchvision.models.mnasnet1_3()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    mnasnet1_3_random = PytorchWrapper(identifier='mnasnet1_3_random', model=mnasnet1_3_random, preprocessing=preprocessing)
    mnasnet1_3_random.image_size = 224
    return mnasnet1_3_random


def load_shufflenet_v2_x0_5():
    shufflenet_v2_x0_5 = torchvision.models.shufflenet_v2_x0_5(weights='IMAGENET1K_V1')
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    shufflenet_v2_x0_5 = PytorchWrapper(identifier='shufflenet_v2_x0_5', model=shufflenet_v2_x0_5, preprocessing=preprocessing)
    shufflenet_v2_x0_5.image_size = 224
    return shufflenet_v2_x0_5


def load_random_shufflenet_v2_x0_5():
    shufflenet_v2_x0_5_random = torchvision.models.mnasnet1_3()
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    shufflenet_v2_x0_5_random = PytorchWrapper(identifier='shufflenet_v2_x0_5_random', model=shufflenet_v2_x0_5_random, preprocessing=preprocessing)
    shufflenet_v2_x0_5_random.image_size = 224
    return shufflenet_v2_x0_5_random








