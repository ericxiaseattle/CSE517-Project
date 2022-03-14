import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KernelDensity

def main():
    prefix = 'decsum/results/models_experiments/sentence_select/selected_sentence/yelp/50reviews/test/Transformer/'
    file = prefix + 'window_1' + '/order/10000/text_.csv'

    df = pd.read_csv(file)
    preds = np.asarray(df['pred'].tolist())
    fig, ax = plt.subplots()
    kde = sns.kdeplot(preds, ax=ax, bw_method=0.1)
    x, y = kde.lines[0].get_data()

    plt.xlabel('Model prediction')
    ax.set_xlim(0, 6)
    ax.set_xticks(range(1, 6))
    ax.set_ylim(-0.015, 0.6)
    ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    plt.hlines(y=0.0, xmin=0, xmax=min(x))
    plt.hlines(y=0.0, xmin=max(x), xmax=6)
    plt.title('Example Summaries for iHOP Restaurant')

    # We arbitrarily chose the circles and stars representing selected sentences with DecSum and PreSumm on the plot, 
    # as we couldn't figure out how these sentences were chosen in the original paper
    first, second, third = np.where(x>2)[0][0], np.where(x>4)[0][0], np.where(x>4.4)[0][0]
    decsum_dots = [x[first], x[second], x[third]], [y[first], y[second], y[third]]
    plt.plot(decsum_dots[0], decsum_dots[1], 'o', color='C0', ms=10, label='DecSum')

    first, second, third, fourth, fifth = np.where(x>3.2)[0][0], np.where(x>4.2)[0][0], np.where(x>4.25)[0][0], \
                                        np.where(x>4.5)[0][0], np.where(x>4.6)[0][0]
    presumm_dots = [x[first], x[second], x[third], x[fourth], x[fifth]], \
                [y[first], y[second], y[third], y[fourth], y[fifth]]
    plt.plot(presumm_dots[0], presumm_dots[1], '*', color='green', ms=10, label='PreSumm')

    plt.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    main()
