"""This script is a demo file to Compare model activations and neural network activate
    on many dataset from Brainscore vision library.
..moduleauthor:: Marius THORRE
"""

import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(current_dir, '../'))
if project_path not in sys.path:
    sys.path.append(project_path)

import seaborn
import brainscore_vision
from brainscore_vision.benchmark_helpers.neural_common import average_repetition
import warnings

from imagebraindl.dataset.dataset import preprocess_FreemanZiemba2013
import imagebraindl.learning.model as model
from imagebraindl.layer_analyse.layer_analyse import get_score

warnings.filterwarnings("ignore")

if __name__ == "__main__":
    neural_data = brainscore_vision.load_dataset("Geirhos2021_cue-conflict")
    neural_data = neural_data.transpose('presentation')

    V4_data = neural_data.sel(region='V1')
    V4_data = average_repetition(V4_data)
    V4_data = V4_data.squeeze('time_bin')

    IT_data = neural_data.sel(region='IT')
    IT_data = average_repetition(IT_data)
    IT_data = IT_data.squeeze('time_bin')

    neural_data = brainscore_vision.load_dataset("FreemanZiemba2013.public")
    V1_data = preprocess_FreemanZiemba2013(neural_data, 'V1')
    V2_data = preprocess_FreemanZiemba2013(neural_data, 'V2')

    alexnet = model.load_alexnet()
    alexnet_random = model.load_alexnet_random()

    # squeezenet = model.load_squeezenet()
    # squeezenet_random = model.load_squeezenet_random()

    # vgg16 = model.load_vgg16()
    # vgg16_random = model.load_random_vgg16()

    # vgg19 = model.load_vgg19()
    # vgg19_random = model.load_random_vgg19()

    # googlenet = model.load_googlenet()
    # googlenet_random = model.load_random_googlenet()

    # resnet = model.load_resnet()
    # resnet_random = model.load_random_resnet()

    # googlenet = model.load_googlenet()
    # googlenet_random = model.load_random_googlenet()

    # inception = model.load_inception()
    # inception_random = model.load_random_inception()

    # mobilenet = model.load_mobilenet()
    # mobilenet_random = model.load_random_mobilenet()

    # densenet = model.load_densenet()
    # densenet_random = model.load_random_densenet201()

    # efficient = model.load_efficientnet_b7()
    # efficient_random = model.load_random_efficientnet_b7()

    # convnet = model.load_convnet()
    # convnet_random = model.load_random_convnet_large()

    simple_model = [alexnet]
    random_model = [alexnet_random]
    name_model = ["alexnet"]

    model_layers = ['features.2', 'features.7', 'features.12']

    for idx, model in enumerate(simple_model):
        res_df = get_score(
            model_name=name_model[idx],
            model=model,
            model_layers=model_layers,
            random_model=random_model[idx],
            V1_data=V1_data,
            V2_data=V2_data,
            IT_data=IT_data,
            V4_data=V4_data,
            path=f"{name_model[idx]}VSventralstream.txt"
        )

        print(res_df.head())

        g = seaborn.catplot(
            data=res_df,
            y='score',
            x='layer',
            hue='model',
            col='region',
            kind='bar',
            col_order=['V4', 'IT'],
            sharey=False
        )

        g.savefig(f"{name_model[idx]}-FreemanZiemba2013.png")
