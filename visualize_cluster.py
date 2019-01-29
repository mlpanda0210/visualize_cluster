#どのように分類されたか可視化
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt

def visualize_cluster(reduced,pred):
    target_names = set(pred)
    colors = str('rgbcmyk')
    markers=str("o+x^v")

    echo_colors = colors*len(markers)
    echo_markers = str()
    for marker in markers:
        echo_markers += marker*len(colors)


    target_ids = list(target_names)
    plt.figure()
    for i, c,m, label in zip(target_ids, echo_colors,echo_markers, target_names):
        plt.scatter(reduced[pred == i, 0], reduced[pred == i, 1],
                        c=c, marker =m, label=label,s=2)
    plt.legend()
    plt.show()
