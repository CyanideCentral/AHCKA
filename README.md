# AHCKA
Code for attributed hypergraph clustering and four datasets (in "data" folder).

## Pre-requisites
numpy, scipy, scikit-learn, scann

Install with: pip install {library_name}

## Test large-scale datasets
We provide links to the original data.

Amazon: https://nijianmo.github.io/amazon/index.html

MAG-PM (OAG v2): https://www.aminer.org/oag2019

## Usage
python AHCKA.py --dataset cora --data coauthorship

python AHCKA.py --dataset cora --data cocitation

python AHCKA.py --dataset citeseer --data cocitation

python AHCKA.py --dataset dblp --data coauthorship

(The following lines need large-scale datasets and ScaNN indices)

python AHCKA.py --dataset amazon --data npz --scale --beta 0.4 --interval 1

python AHCKA.py --dataset magpm --data npz --scale --beta 0.4