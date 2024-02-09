# Step 3. Extending the functionality
Let's make the segmentation method a bit more advanced!

## 3. Implement adaptive segmentation.
Finish the function `updateSamples()`.

This function lets us update the model by replacing a fraction of the existing `old_samples` with some `new_samples`.
This will make the model gradually change over time, and we are able to control the rate of how fast it changes by adjusting the `update_ratio` argument.
The `update_ratio` should be a number between 0 and 1, where 0.1 means that a random 10% of `old_samples` are being replaced with new one each iteration.

Keypress <kbd>a</kbd> activates/deactivates the adaptive functionality.

In its current state, this method does not perform any update at all.
Your job is to implement this method so that it works as intended.

**Suggestion 1:**  You can for instance use [cv::randu] to generate a matrix of random numbers between 0 and 1 with the
same size as `new_samples_`. For each pixel in the randomized matrix where the random number is smaller than `update_ratio`,
copy the value from `new_samples` to `old_samples` at the corresponding pixel position.

**Suggestion 2:** Another approach is to make use of [cv::randShuffle]. By first shuffling both `samples_` and `new_samples` you
can update the first N columns of `samples_` with the first N columns of `new_samples`. Here N should be determined based
on the `update_ratio`.

How does this adaptive model work? Try adjusting the `update_ratio`. Are the changes noticeable?

## 4. Clean up the segmentation with morphological operations
Go to the function `performSegmentation()`.

Clean up the segmentation by using morphological operations on the binary image.
[cv::morphologyEx] can be used for this.

Connected component analysis [cv::connectedComponentsWithStats] can be used to identify the largest connected component in the binary image and remove the smaller ones.


## 5. Extract better and more features
Go to the function `extractFeatures()`.

Try changing the color representation of the image from **RGB** to [some other color space][color conversions].
Does it make any difference for the segmentation?
(I like `YCrCb`).

Take a look at [cv::cvtColor].

Try using more than 3 features per pixel.
- Measures of local uniformity
    - Local standard deviation
    - Local entropy
- Other ideas?


## 6. Compute contours of the segmented objects and extract interesting features
In OpenCV you can use the contour of segmented areas to compute a set of different features of that object, such as center of mass, orientation, area and so on.
You can even fit ellipses or lines to your objects.

Take a look at the following OpenCV tutorials and experiment with feature extraction based on contours!
- [Contours: Getting Started]
- [Contour Features]
- [Contour Properties]
- [Some C++ examples]


## 7. Use the segmentation method
Here are some suggestions:
- Insert a background image in the segmented area (like with a green screen)
- Track the pixel coordinates of a coloured object
- Estimate the contours of the table/floor or some object

[cv::randu]: https://docs.opencv.org/4.5.5/d2/de8/group__core__array.html#ga1ba1026dca0807b27057ba6a49d258c0
[cv::randShuffle]: https://docs.opencv.org/4.5.5/d2/de8/group__core__array.html#ga6a789c8a5cb56c6dd62506179808f763
[cv::morphologyEx]: https://docs.opencv.org/4.5.5/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f
[cv::connectedComponentsWithStats]: https://docs.opencv.org/4.5.5/d3/dc0/group__imgproc__shape.html#gae57b028a2b2ca327227c2399a9d53241
[color conversions]: https://docs.opencv.org/4.5.5/de/d25/imgproc_color_conversions.html
[cv::cvtColor]: https://docs.opencv.org/4.5.5/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab

[Contours: Getting Started]: https://docs.opencv.org/4.9.0/d4/d73/tutorial_py_contours_begin.html
[Contour Features]: https://docs.opencv.org/4.9.0/dd/d49/tutorial_py_contour_features.html
[Contour Properties]: https://docs.opencv.org/4.9.0/d1/d32/tutorial_py_contour_properties.html
[Some C++ examples]: https://docs.opencv.org/4.9.0/d7/da8/tutorial_table_of_content_imgproc.html
