# TheFunBox
The Fun Box is just a cool little box of some basic tools for Array Scaling and Statistics: \
This is a sample package I did for school, please do not take this seriously.
# Documentation
## [Installation](https://github.com/emmettgb/TheFunBox#installation)
## [Stats](https://github.com/emmettgb/TheFunBox#stats)
### [Stats.Base](https://github.com/emmettgb/TheFunBox#statsbase)
#### [Stats.Base.mean](https://github.com/emmettgb/TheFunBox#statsbasemeanarray)
#### [Stats.Base.variance](https://github.com/emmettgb/TheFunBox#statsbasevariancearray)
#### [Stats.Base.standard_deviation(array)](https://github.com/emmettgb/TheFunBox#statsbasestandard_deviationarray)
### [Stats.Inferential](https://github.com/emmettgb/TheFunBox#statsinferential)
#### [Stats.Inferential.student_t](https://github.com/emmettgb/TheFunBox#statsinferentialstudent_tsamplegeneral)
#### [Stats.Inferential.student_f](https://github.com/emmettgb/TheFunBox#statsinferentialstudent_fsamplegeneral)
### [Stats.Bayesian](https://github.com/emmettgb/TheFunBox#statsbayesian)
#### [Stats.Bayesian.bay_ther](https://github.com/emmettgb/TheFunBox#statsbayesianbay_therprobabilitypriorevidence)
#### [Stats.Bayesian.cond_prob](https://github.com/emmettgb/TheFunBox#statsbayesiancond_probprobabilitypriorevidence)
## [Scalars](https://github.com/emmettgb/TheFunBox#scalars)
### [Scalars.ArrayScale](https://github.com/emmettgb/TheFunBox#scalarsarrayscale)
#### [Scalars.ArrayScale.arbritrary_rescale](https://github.com/emmettgb/TheFunBox#scalarsarrayscalearbritrary_rescalearray)
#### [Scalars.ArrayScale.standardize](https://github.com/emmettgb/TheFunBox#scalarsarrayscalestandardizearray)
#### [Scalars.ArrayScale.mean_normalize](https://github.com/emmettgb/TheFunBox#scalarsarrayscalemean_normalizearray)
# Installation
To install TheFunBox with pip: \
pip3 install -i https://test.pypi.org/simple/ TheFunBox \
# Stats
## Stats.Base
Wow, this is the biggest class in this module. 3 methods.
### Stats.Base.mean(array)
Divides the summatation of an array by the number of samples in the array.
```python
>>> array = 4,7,8,6,5,3
>>> Stats.Base.mean(array)
5.5

```
### Stats.Base.variance(array)
Gives The variance of an array.

### Stats.Base.standard_deviation(array)
Takes an array, and provides the standard deviation
```python
>>> array = 4,7,8,6,5,3

```
## Stats.Inferential
Definitely not only 2 methods
```python
>>> array = 4,7,8,6,5,3

```
### Stats.Inferential.student_t(sample,general)
Performs a T test with sample and general data, returns a P value.
```python
>>> array = 4,7,8,6,5,3

```
### Stats.Inferential.student_f(sample,general)
Performs an F test with the sample and general data, returns a P value. The hipster inferential statisticians really like this, and I had a Julia function for it, so I was like why not.
```python
>>> array = 4,7,8,6,5,3

```
## Stats.Bayesian
Bayesian Statistics for the minimilist
```python
>>> array = 4,7,8,6,5,3

```
### Stats.Bayesian.bay_ther(probability,prior,evidence)
Returns a posterior out of three integers representing percentages in data. Returns an unconverted percentage as a float.
```python
>>> array = 4,7,8,6,5,3

```
### Stats.Bayesian.cond_prob(probability,prior,evidence)
Returns a conditional probability posterior out of three integers representing percentages in data, returns an unconverted percentage as a float.
```python
>>> array = 4,7,8,6,5,3

```
# Scalars
## Scalars.ArrayScale
### Scalars.ArrayScale.arbritrary_rescale(array)
Returns an array that is arbritrary rescaled, what else did you expect?
```python
>>> array = 4,7,8,6,5,3

```
### Scalars.ArrayScale.standardize(array)
Returns a standardized (StandardScalar) array.
```python
>>> array = 4,7,8,6,5,3

```
### Scalars.ArrayScale.mean_normalize(array)
Normalizes the data based on the mean. I found this formula on Wikipedia.
```python
>>> array = 4,7,8,6,5,3

```
