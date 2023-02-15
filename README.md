# Real-time learning and segmentation
Welcome to this lab in the computer vision course [TEK5030] at the University of Oslo.
In this lab we will experiment with real time image segmentation on image streams from a camera or a prerecorded video.

Start by cloning this repository on your machine and set up your project using conan (see below).
If you want to use prerecorded video, you can download the [videos](https://www.uio.no/studier/emner/matnat/its/TEK5030/v19/resurser/lab_11_videos.zip)
(259MB) and unzip them somewhere convenient on your computer[&ast;](#terminal).
Then open the lab project in your editor.

The lab is carried out by following these steps:
1. [Get an overview](lab-guide/1-get-an-overview.md)
2. [Implement simple color-based segmentation](lab-guide/2-implement-simple-color-based-segmentation.md)
3. [Further work](lab-guide/3-further-work.md)

You will find our proposed solution at https://github.com/tek5030/solution-segmentation.
But please try to solve the lab with help from others instead of just jumping straight to the solution ;)

Start the lab by going to the [first step](lab-guide/1-get-an-overview.md).


## Prerequisites
- [Ensure Conan is installed on your system][conan], unless you are not on a lab computer.
- Install project dependencies using conan:

   ```bash
   # git clone https://github.com/tek5030/lab-segmentation.git
   # cd lab-segmentation

   conan install . --install-folder=build --build=missing
   ```
- When you configure the project in CLion, remember to set `build` as the _Build directory_, as described in [lab_intro].

---

##### &ast; Download videos using terminal
<a name="terminal"></a>
```bash
wget https://www.uio.no/studier/emner/matnat/its/TEK5030/v19/resurser/lab_11_videos.zip
unzip lab_11_videos.zip
rm lab_11_videos.zip
```
