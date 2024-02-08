# Real-time learning and segmentation
Welcome to this lab in the computer vision course [TEK5030] at the University of Oslo.
In this lab we will experiment with real time image segmentation on image streams from a camera or a prerecorded video.

Start by cloning this repository on your machine.

If you want to use prerecorded video, you can download the [videos]
(259MB) and unzip them somewhere convenient on your computer[&ast;](#terminal).

Then open the lab project in CLion using the cmake-file in the base directory: `lab-segmentation/CMakeLists.txt`.
If you are uncertain about how this is done, please take a look at [the intro lab].

The lab is carried out by following these steps:
1. [Get an overview](lab-guide/1-get-an-overview.md)
2. [Implement simple color-based segmentation](lab-guide/2-implement-simple-color-based-segmentation.md)
3. [Further work](lab-guide/3-further-work.md)

You will find our proposed solution at https://github.com/tek5030/solution-segmentation,
but please try to solve the lab with help from others instead of just jumping straight to the solution ;)

Start the lab by going to the [first step](lab-guide/1-get-an-overview.md).

## Prerequisites
- OpenCV must be installed on your system. If you are on a lab computer, you are all set.

  If you are on Ubuntu, but not on a lab computer, the following should be sufficient _for this lab_.

   ```bash
   sudo apt update
   sudo apt install libopencv-dev
   ```

- We refer to [setup_scripts](https://github.com/tek5030/setup_scripts) and [the intro lab] as a general getting started-guide for the C++ labs on Ubuntu 22.04.

[the intro lab]: https://github.com/tek5030/lab-intro/blob/master/cpp/lab-guide/1-open-project-in-clion.md

---

##### &ast; Download videos using terminal
<a name="terminal"></a>
```bash
wget https://www.uio.no/studier/emner/matnat/its/TEK5030/v19/resurser/lab_11_videos.zip
unzip lab_11_videos.zip
rm lab_11_videos.zip
```

[TEK5030]: https://www.uio.no/studier/emner/matnat/its/TEK5030/
[videos]: https://www.uio.no/studier/emner/matnat/its/TEK5030/v19/resurser/lab_11_videos.zip
[conan]: https://tek5030.github.io/tutorial/conan.html
[lab_intro]: https://github.com/tek5030/lab-intro/blob/master/cpp/lab-guide/1-open-project-in-clion.md#6-configure-project
