import os
import shutil
import pandas as pd
from brainscore_vision import load_metric

cache_dir = "C:\\Users\\thorr\\.result_caching"
rdm_metric = load_metric('rdm')


def get_score(
        model,
        model_layers,
        model_name,
        random_model,
        IT_data,
        V1_data,
        V2_data,
        V4_data,
        path,
):
    scores = {'model': [], 'layer': [], 'region': [], 'score': []}

    stimulus_set_IT_V4 = IT_data.stimulus_set

    for model, model_id in [(model, model_name), (random_model, f'{model_name}_random')]:
        print(model_id)
        for layer in model_layers:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
            print(layer)
            model_activations = model(stimulus_set_IT_V4, layers=[layer])
            print(f'computing representational similarity between IT activations and layer {layer} activations')
            score_it = rdm_metric(assembly1=IT_data, assembly2=model_activations)
            scores['model'].append(model_id)
            scores['layer'].append(layer)
            scores['region'].append('IT')
            scores['score'].append(score_it.values.item())

            print(f'computing representational similarity between V4 activations and layer {layer} activations')
            score_v4 = rdm_metric(assembly1=V4_data, assembly2=model_activations)
            scores['model'].append(model_id)
            scores['layer'].append(layer)
            scores['region'].append('V4')
            scores['score'].append(score_v4.values.item())

    stimulus_set_V1_V2 = V1_data.stimulus_set

    for model, model_id in [(model, model_name), (random_model, f'{model_name}_random')]:
        print(model_id)
        for layer in model_layers:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
            print(layer)
            model_activations = model(stimulus_set_V1_V2, layers=[layer])
            print(f'computing representational similarity between V1 activations and layer {layer} activations')
            score_v1 = rdm_metric(assembly1=V1_data, assembly2=model_activations)
            scores['model'].append(model_id)
            scores['layer'].append(layer)
            scores['region'].append('V1')
            scores['score'].append(score_v1.values.item())

            print(f'computing representational similarity between V2 activations and layer {layer} activations')
            score_v2 = rdm_metric(assembly1=V2_data, assembly2=model_activations)
            scores['model'].append(model_id)
            scores['layer'].append(layer)
            scores['region'].append('V2')
            scores['score'].append(score_v2.values.item())

    res_df = pd.DataFrame(scores)
    res_df.to_csv(path, index=False)
    return res_df


