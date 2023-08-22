# AHCKA: Efficient and Effective Attributed Hypergraph Clustering via K-Nearest Neighbor Augmentation (SIGMOD 2023)

[Link to our paper](https://dl.acm.org/doi/abs/10.1145/3589261)

If you use our code or data, please cite:

    @article{LiYS23,
      author       = {Yiran Li and
                      Renchi Yang and
                      Jieming Shi},
      title        = {Efficient and Effective Attributed Hypergraph Clustering via K-Nearest
                      Neighbor Augmentation},
      journal      = {Proc. {ACM} Manag. Data},
      volume       = {1},
      number       = {2},
      pages        = {116:1--116:23},
      year         = {2023}
    }

This repository contains the implementation of AHCKA algorithm for attributed hypergraph clustering and the eight datasets used in our experiments.

## Pre-requisites
numpy, scipy, scikit-learn, scann

Install with: `pip install {library_name}`

## Optional: large-scale datasets
Processed Amazon and MAG-PM datasets can be downloaded at: https://www.dropbox.com/s/y875ig3ng2ft9jr/AHCKA-data.zip?dl=0

Original data can be accessed via the following links.

Amazon: https://nijianmo.github.io/amazon/index.html

MAG-PM (OAG v2): https://www.aminer.org/oag2019

## Usage

###### Query
`python AHCKA.py --dataset query --data npz`

###### Cora-CA
`python AHCKA.py --dataset cora --data coauthorship`

###### Cora-CC
`python AHCKA.py --dataset cora --data cocitation`

###### Citeseer
`python AHCKA.py --dataset citeseer --data cocitation`

###### 20News
`python AHCKA.py --dataset 20news --data npz`

###### DBLP
`python AHCKA.py --dataset dblp --data coauthorship`

*Note: the following tests require large-scale datasets and ScaNN indices.*

###### Amazon
`python AHCKA.py --dataset amazon --data npz --scale --beta 0.4 --interval 1`

###### MAG-PM
`python AHCKA.py --dataset magpm --data npz --scale --beta 0.4`


