"""
CSCC11 - Introduction to Machine Learning, Winter 2022, Assignment 3
B. Chan, E. Franco, D. Fleet

This file specifies the hyperparameters for the two real life datasets.
Note that different hyperparameters will affect the runtime of the 
algorithm.
"""

# ====================================================
# TODO: Use Validation Set to Tune hyperparameters for the Amazon dataset
# Use Optimal Parameters to get good accuracy on Test Set
AMAZON_HYPERPARAMETERS = {
    # NOTE: 10000 takes quite a while to run. Suppose if we ever want to modify the code again,
    #       we could parallelize the code such that each tree is constructed in parallel (why not right?)
    "num_trees": 395,
    "features_percent": 0.01,
    "data_percent": 0.60,
    "max_depth": 9,
    "min_leaf_data": 20,
    "min_entropy": 0.14,
    "num_split_retries": 10
}
# ====================================================

# ====================================================
# TODO: Use Validation Set to Tune hyperparameters for the Titanic dataset
# Use Optimal Parameters to get good accuracy on Test Set
TITANIC_HYPERPARAMETERS = {
    "num_trees": 15,
    "features_percent": 0.8,
    "data_percent": 0.8,
    "max_depth": 12,
    "min_leaf_data": 10,
    "min_entropy": 0.125,
    "num_split_retries": 10
}
# ====================================================
