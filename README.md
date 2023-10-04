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

### Optional: large-scale datasets
Processed Amazon and MAG-PM datasets, with constructed ScaNN indices, can be downloaded at: https://www.dropbox.com/s/y875ig3ng2ft9jr/AHCKA-data.zip?dl=0

Original Amazon and MAG data can be accessed via the following links.

Amazon: https://nijianmo.github.io/amazon/index.html

MAG (OAG v2): https://www.aminer.org/oag2019

## Usage

To run AHCKA clustering algorithm on a dataset, please specify the type of dataset by command-line parameter `--data` and its name by `--dataset`. Datasets supported by our implementation include the following:

| Type of dataset                           |    --data    |          --dataset         |
|-------------------------------------------|:------------:|:--------------------------:|
| Co-authorship hypergraph in .pickle files | coauthorship |         cora, dblp         |
| Co-citation hypergraph in .pickle files   |  cocitation  |       cora, citeseer       |
| Attributed hypergraph stored in .npz file |      npz     | query, 20news, amazon, magpm |

Other parameters are optional:

| Parameter  | Default | Description                                           |
|------------|---------|-------------------------------------------------------|
| --knn_k    | 10      | $K$, the size of neighborhood in KNN graph              |
| --alpha    | 0.2     | $\alpha$, restart probability in random walk with restart (RWR) |
| --beta     | 0.5     | $\beta$, the weight of KNN random walk                         |
| --tmax     | 200     | $T_{a}$, the maximum number of orthogonal iterations           |
| --interval | 5       | $\tau$, the interval of computing discrete cluster labels |
| --scale    | -       | Apply settings for large-scale data: approximate KNN with ScaNN; simplified initialization ($T_i$=1) |
| --rd_init | -       | Initialize cluster labels at random |
| --seeds    | 0       | Random seed, only effective with --rd_init on |
| --verbose  | -       | Produce verbose command-line output                   |

To **reproduce** the results in our paper, please use the following commands for corresponding datasets.

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

*Note: the following tests require downloading optional large-scale datasets with constructed ScaNN indices.*

###### Amazon
`python AHCKA.py --dataset amazon --data npz --scale --beta 0.4 --interval 1`

###### MAG-PM
`python AHCKA.py --dataset magpm --data npz --scale --beta 0.4`

Sample output of AHCKA, on Cora co-authorship dataset:
```
Acc=0.651 F1=0.608 NMI=0.462 ARI=0.406 Time=0.470s RAM=221MB
```
