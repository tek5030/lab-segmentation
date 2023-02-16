#include "multivariate-normal-model.h"
#include "opencv2/imgproc.hpp"

MultivariateNormalModel::MultivariateNormalModel(const cv::Mat& samples)
{
  performTraining(samples);
}


void MultivariateNormalModel::performTraining(const cv::Mat& samples)
{
  // TODO 1.1: Train the multivariate normal model by estimating the mean and covariance given the samples.
  mean_ = cv::Mat::ones(1, samples.cols, CV_32F);                 // Dummy, replace
  covariance_ = cv::Mat::eye(samples.cols, samples.cols, CV_32F); // Dummy, replace

  // We are going to compute the inverse of the estimated covariance,
  // so we must ensure that that the matrix is indeed invertible (not singular).
  if (cv::abs(cv::determinant(covariance_)) < 1e-14)
  {
    covariance_ += cv::Mat::eye(covariance_.size(), CV_32F)*1e-3;
  }

  // TODO 1.2: Compute the inverse of the estimated covariance.
  inverse_covariance_ = cv::Mat::eye(samples.cols, samples.cols, CV_32F);  // Dummy, replace
}


cv::Mat MultivariateNormalModel::computeMahalanobisDistances(const cv::Mat& image) const
{
  // Convert to double precision and reshape to feature vector rows.
  cv::Mat float_image;
  image.convertTo(float_image, CV_32F);
  const auto num_samples = float_image.total();
  float_image = float_image.reshape(1, static_cast<int>(num_samples));

  cv::Mat mahalanobis_img(image.size(), CV_32F);

  // TODO 2: Compute the mahalanobis distance for each pixel feature vector wrt the multivariate normal model.
  mahalanobis_img.setTo(std::numeric_limits<float>::infinity());

  return mahalanobis_img;
}


cv::Mat MultivariateNormalModel::mean() const
{
  return mean_.clone();
}


cv::Mat MultivariateNormalModel::covariance() const
{
  return covariance_.clone();
}


cv::Mat MultivariateNormalModel::inverseCovariance() const
{
  return inverse_covariance_.clone();
}
