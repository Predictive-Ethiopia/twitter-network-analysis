import pandas as pd


def df_tostring(df, rows=None):
    return f'  shape: {df.shape}\n' \
        f'  dataframe ({"first " + str(rows) if rows else "all"} rows):\n{df.head(rows).to_string()}\n'


def graph_tostring(graph, nodes=None, edges=None):
    return f'  shape: ({len(graph.nodes)}, {len(graph.edges)})\n' \
        f'  nodes ({"first " + str(nodes) if nodes else "all"} nodes): ' \
        f'{str(list(graph.nodes(data=True))[:nodes])}\n' \
        f'  edges ({"first " + str(edges) if edges else "all"} edges): ' \
        f'{str(list(graph.edges(data=True))[:edges])}\n'


def nodes_to_dataframe(g):
    return pd.DataFrame.from_dict(dict(g.nodes(data=True))).transpose()


# [0.25, 0.5, 0.75] -> [(0.25, 0.5), (0.25, 0.75), (0.5, 0.75)]
def pairwise_combinations(l):
    return [(x, e) for i, x in enumerate(l[:-1]) for e in l[i + 1:]]


def pass_results_pipeline(from_results, to_results, r_names):
    # print(from_results)
    for name in r_names:
        to_results[0][name] = from_results[0][name]
        to_results[1][name] = from_results[1][name]

    return to_results


def pass_results_orchestrator(from_results, to_results, r_names):
    for dataset_name in from_results.keys():
        to_results[dataset_name] =\
            pass_results_pipeline(from_results[dataset_name], to_results[dataset_name], r_names)

    return to_results


def remove_results_orchestrator(results):
    return {dataset_name: (None, dataset_result[1])
            for dataset_name, dataset_result in results.items()}
