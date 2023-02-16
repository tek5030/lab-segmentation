# Step 2: Implement simple colour-based segmentation
First, if you haven't done so already, please read through the files to get an overview of the lab.

## 1. Implement the method `MultivariateNormalModel::performTraining()`
The multivariate normal distribution is characterized by a mean vector **&mu;** and a covariance matrix **&Sigma;**.

![\mathcal{N}(\mathbf{x}; \boldsymbol{\mu}, \boldsymbol{\Sigma}) =
\frac{1}{ (2\pi)^{\frac{k}{2}} \left|\boldsymbol{\Sigma}\right|^{\frac{1}{2}}}
\exp\left[-\textstyle\frac{1}{2}(\boldsymbol{\mu} - \mathbf{x})^{T}\boldsymbol{\Sigma}^{-1}
(\boldsymbol{\mu} - \mathbf{x}) \right]](img/multivariate_normal_distribution.png)

The method `MultivariateNormalModel::performTraining()` should estimate the mean `mean_` and the covariance `covariance_` for the model based on the training samples in the matrix `samples` collected from the sampling region.

It must also compute the inverse of the covariance matrix `inverse_covariance_`, which we will later use to compute the Mahalanobis distance.

Hints:
- Take a look at [cv::Mahalanobis].
- What is the shape of the `samples` matrix? Take a look at [cv::CovarFlags]. Flags can be combined like this: `flag1|flag2`.

## 2. Implement the method `MultivariateNormalModel::computeMahalanobisDistances`
Given a multivariate normal model, the Mahalanobis distance for a vector **x** is a measure of how well the vector fits with the model.

![\mathit{d}_{\mathit{M}}(\mathbf{x}) = \sqrt{(\mathbf{x}-\boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1}
(\mathbf{x} - \boldsymbol{\mu})}](img/mahalanobis_distance.png)

This method should compute the Mahalanobis distance between every pixel in the input image and the estimated multivariate
normal model described by `mean_` and `inverse_covariance_` and return an image of Mahalanobis distances.

For tips about how to iterate `cv::Mat`s, you may take a look at the [OpenCV tutorials].

## Experiment!
Now you should have a working segmentation method, and it is finally time to play around with it!

For example:
- Try it out on different colours/surfaces. How well does it work?
- Try changing the threshold manually using the slider.
- As we know, Otsu's method estimates a threshold between modes in a bimodal histogram distribution.
  Check out how well Otsu's method estimates a decent threshold by pressing `o`.
  When does Otsu's work well, and when is the threshold estimate bad?
  Why?


You can now continue to the [next step](3-further-work.md) to make it a bit more advanced.

[cv::calcCovarMatrix]: https://docs.opencv.org/4.5.5/d2/de8/group__core__array.html#gae6ffa9354633f984246945d52823165d
[cv::CovarFlags]: https://docs.opencv.org/4.5.5/d0/de1/group__core.html#ga719ebd4a73f30f4fab258ab7616d0f0f
[cv::invert]: https://docs.opencv.org/4.5.5/d2/de8/group__core__array.html#gad278044679d4ecf20f7622cc151aaaa2
[cv::Mahalanobis]: https://docs.opencv.org/4.5.5/d2/de8/group__core__array.html#ga4493aee129179459cbfc6064f051aa7d
[OpenCV tutorials]: https://docs.opencv.org/4.5.5/db/da5/tutorial_how_to_scan_images.html