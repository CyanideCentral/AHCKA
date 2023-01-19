# AHCKA
Code for attributed hypergraph clustering and six datasets (in "data" folder).

## Pre-requisites
numpy, scipy, scikit-learn, scann

Install with: `pip install {library_name}`

## Test large-scale datasets
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

*The following tests require large-scale datasets and ScaNN indices*

###### Amazon
`python AHCKA.py --dataset amazon --data npz --scale --beta 0.4 --interval 1`

###### MAG-PM
`python AHCKA.py --dataset magpm --data npz --scale --beta 0.4`