# Similarity Metric

This repository contains a simple Python implementation of a similarity metric.

The metric function is implemented in:

```text
similarity.py
````

An example of how to call the function is provided in:

```text
main.py
```

## Metric formula

The similarity metric is calculated as:

```math
A = \exp\left(-\left(\prod_{j=1}^{n} |x_j - y_j|\right)^{\frac{1}{n}}\right)
```

where:

* (x_j) is the j-th value from the first list
* (y_j) is the j-th value from the second list
* (n) is the length of the lists
* both input lists must have the same length
* (d(x_j, y_j) = |x_j - y_j|)

The metric can also be interpreted as:

```math
A = \exp\left(-\text{geometric mean of absolute differences}\right)
```

## Repository structure

```text
.
├── similarity.py
├── main.py
└── README.md
```

## Usage

Import the metric class from `similarity.py`:

```python
from similarity import SimilarityMetric
```

Create the metric object and calculate the similarity between two lists:

```python
from similarity import SimilarityMetric

metric = SimilarityMetric()

first_list = [1.2, 2.5, 3.1, 4.0]
second_list = [1.0, 2.8, 3.0, 3.6]

A = metric.calculate(first_list, second_list)

print(A)
```

## Dataset

This repository does not contain the dataset.

The expected dataset structure is a table where each row represents a measurement for one patient, one method, and one point.

Expected columns:

```text
Patient_ID
Method
Point
R-L_Component
A-P_Component
S-I_Component
3D
```

Example structure:

```text
Patient_ID | Method   | Point | R-L_Component | A-P_Component | S-I_Component | 3D
1          | CBCT     | 1     | -2.181        | -0.421        | -0.434        | 2.264
1          | CBCT     | 2     | -1.531        | -0.018        | 0.785         | 1.720
1          | MOLAR    | 1     | -0.893        | -0.480        | 0.010         | 1.014
1          | LANDMARK | 1     | -1.723        | -0.775        | -0.216        | 1.901
```

The `Method` column contains the registration or measurement method, for example:

```text
CBCT
MOLAR
LANDMARK
BEST FIT
```

The component columns contain numeric values used for similarity calculations.

## Notes

The function takes two lists or array-like objects as input.

Both input lists must:

* contain numeric values
* have the same length
* not be empty

