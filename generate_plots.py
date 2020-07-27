from matplotlib import pyplot as plt

from County import County


def _get_datasets(county, dataset_names):
    datasets = []
    dataset_labels = []
    if 'active' in dataset_names:
        datasets.append(county.active)
        dataset_labels.append('Active Cases')
    if 'confirmed' in dataset_names:
        datasets.append(county.confirmed)
        dataset_labels.append('Confirmed Cases')
    if 'deaths' in dataset_names:
        datasets.append(county.deaths)
        dataset_labels.append('Deaths')
    if 'recovered' in dataset_names:
        datasets.append(county.recovered)
        dataset_labels.append('Recoveries')
    if 'new' in dataset_names:
        datasets.append(county.new_per_day)
        dataset_labels.append('New Cases')
    return county.dates, datasets, dataset_labels


def generate_plot(county, datasets):
    colors = ['black', 'red', 'blue', 'green', 'orange', 'purple']

    dates, datasets, dataset_labels = _get_datasets(county, datasets)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    # Iterate through different datasets
    for i in range(len(datasets)):
        ax1.scatter(dates, datasets[i], s=10, c=colors[i], label=dataset_labels[i])

    plt.xticks([dates[i] for i in range(0, len(dates) + 1, len(dates) // 4)])
    plt.legend(loc='upper left')
    plt.title(county.name.capitalize() + ' County')

    if not path.exists('images'):
        mkdir('images')

    filepath = f'images/{county.name}_{dates[-1]}.png'
    plt.savefig(filepath)
    return filepath