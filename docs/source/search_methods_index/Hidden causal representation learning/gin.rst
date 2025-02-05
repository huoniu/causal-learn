.. _gin:

Generalized Independence Noise (GIN) condition-based method
=============================================================

Algorithm Introduction
-----------------------------------------------------------

Learning the structure of Linear, Non-Gaussian LAtent variable Model (LiNLAM) based the GIN [1]_ condition.

Usage
-----------------------------------------------------------
.. code-block:: python

    from causallearn.search.FCMBased.GIN.GIN import GIN
    G, K = GIN(data)

Parameters
-----------------------------------------------------------
**data**: numpy.ndarray, shape (n_samples, n_features). Data, where n_samples is the number of samples
and n_features is the number of features.

Returns
-----------------------------------------------------------
**G**: GeneralGraph. Causal graph.

**K**: list. Causal Order.

.. [1] Xie, F., Cai, R., Huang, B., Glymour, C., Hao, Z., & Zhang, K. (2020, January). Generalized Independent Noise Condition for Estimating Latent Variable Causal Graphs. In NeurIPS.