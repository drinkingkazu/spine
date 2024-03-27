"""Module to build GNN message passing submodules."""

from mlreco.utils.factory import module_dict, instantiate

from . import layers

__all__ = ['node_layer_construct', 'edge_layer_construct',
           'global_layer_construct']


def node_layer_construct(cfg, node_in, edge_in, glob_in):
    """Instantiates a GNN node update layer from a configuration dictionary.

    Parameters
    ----------
    cfg : dict
        GNN node update layer configuration
    node_in : int
        Number of input node features
    edge_in : int
        Number of input edge features
    glob_in : int
        Number of input global graph features

    Returns
    -------
    object
        Instantiated GNN node update layer
    """
    layer_dict = module_dict(layers, pattern='Node')
    return instantiate(
            layer_dict, cfg, node_in=node_in, edge_in=edge_in, glob_in=glob_in)


def edge_layer_construct(cfg, node_in, edge_in, glob_in):
    """Instantiates a GNN edge update layer from a configuration dictionary.

    Parameters
    ----------
    cfg : dict
        GNN edge update layer configuration
    node_in : int
        Number of input node features
    edge_in : int
        Number of input edge features
    glob_in : int
        Number of input global graph features

    Returns
    -------
    object
        Instantiated GNN edge update layer
    """
    layer_dict = module_dict(layers, pattern='Edge')
    return instantiate(
            layer_dict, cfg, node_in=node_in, edge_in=edge_in, glob_in=glob_in)


def global_layer_construct(cfg, node_in, glob_in):
    """Instantiates a GNN global update layer from a configuration dictionary.

    Parameters
    ----------
    cfg : dict
        GNN global update layer configuration
    node_in : int
        Number of input node features
    glob_in : int
        Number of input global graph features

    Returns
    -------
    object
        Instantiated GNN global update layer
    """
    layer_dict = module_dict(layers, pattern='Global')
    return instantiate(layer_dict, cfg, node_in=node_in, edge_in=edge_in)