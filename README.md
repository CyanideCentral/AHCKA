# AHCKA: Efficient and Effective Attributed Hypergraph Clustering via K-Nearest Neighbor Augmentation

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

## Citation

Welcome to cite our SIGMOD '23 paper if you find this repository helpful.

    @article{li2023efficient,
      title={Efficient and Effective Attributed Hypergraph Clustering via K-Nearest Neighbor Augmentation},
      author={Li, Yiran and Yang, Renchi and Shi, Jieming},
      journal={Proceedings of the ACM on Management of Data},
      volume={1},
      number={2},
      pages={1--23},
      year={2023},
      publisher={ACM New York, NY, USA}
    }
