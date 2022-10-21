# AHCKA
Code for attributed hypergraph clustering and four datasets (in "data" folder).

## Pre-requisites
numpy, scipy, scikit-learn, scann

Install with: `pip install {library_name}`

## Test large-scale datasets
Due to the file size limit of this repository, we provide links to the original data.

Amazon: https://nijianmo.github.io/amazon/index.html

MAG-PM (OAG v2): https://www.aminer.org/oag2019

## Usage

###### Cora-CA
`python AHCKA.py --dataset cora --data coauthorship`

###### Cora-CC
`python AHCKA.py --dataset cora --data cocitation`

###### Citeseer
`python AHCKA.py --dataset citeseer --data cocitation`

###### DBLP
`python AHCKA.py --dataset dblp --data coauthorship`

*The following tests require large-scale datasets and ScaNN indices*

###### Amazon
`python AHCKA.py --dataset amazon --data npz --scale --beta 0.4 --interval 1`

###### MAG-PM
`python AHCKA.py --dataset magpm --data npz --scale --beta 0.4`