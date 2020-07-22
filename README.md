# 3D-R<sup>2</sup>N<sup>2</sup>: 3D Recurrent Reconstruction Neural Network

This repository is an adaptation of the work done in the paper [Choy et al., 3D-R2N2: A Unified Approach for Single and Multi-view 3D Object Reconstruction, ECCV 2016](http://arxiv.org/abs/1604.00449). Given one or multiple views of an object, the network generates voxelized ( a voxel is the 3D equivalent of a pixel) reconstruction of the object in 3D.

[1] *3D-R2N2: A Unified Approach for Single and Multi-view 3D Object Reconstruction*

Choy, Christopher B and Xu, Danfei and Gwak, JunYoung and Chen, Kevin and Savarese, Silvio,
Proceedings of the European Conference on Computer Vision ({ECCV}), 2016 
[arxiv](http://arxiv.org/abs/1604.00449)

## Overview

![Overview](imgs/overview.png)
*Left: images found on Ebay, Amazon, Right: overview of `3D-R2N2`*


In [1], the authors first propose a unified framework for both single and multi-view reconstruction using a `3D Recurrent Reconstruction Neural Network` (3D-R2N2).

| 3D-Convolutional LSTM     | 3D-Convolutional GRU    | Inputs (red cells + feature) for each cell (purple) |
|:-------------------------:|:-----------------------:|:---------------------------------------------------:|
| ![3D-LSTM](imgs/lstm.png) | ![3D-GRU](imgs/gru.png) | ![3D-LSTM](imgs/lstm_time.png)                      |

We can feed in images in random order since the network is trained to be invariant to the order. The critical component that enables the network to be invariant to the order is the `3D-Convolutional LSTM`. The `3D-Convolutional LSTM` selectively updates parts that are visible and keeps the parts that are self-occluded.

![Networks](imgs/full_network.png)

## Results

Please visit the result [visualization page](http://3d-r2n2.stanford.edu/viewer/) to view 3D reconstruction results interactively.


## Datasets

We used [ShapeNet](http://shapenet.cs.stanford.edu) models to generate rendered videos and voxelized models which are available below (you can follow the installation instruction below to extract it to the default directory).

- ShapeNet rendered images [http://cvgl.stanford.edu/data2/ShapeNetRendering.tgz](http://cvgl.stanford.edu/data2/ShapeNetRendering.tgz)
- ShapeNet voxelized models [http://cvgl.stanford.edu/data2/ShapeNetVox32.tgz](http://cvgl.stanford.edu/data2/ShapeNetVox32.tgz)
- Trained ResidualGRUNet Weights [http://cvgl.stanford.edu/data2/ResidualGRUNet.npy](http://cvgl.stanford.edu/data2/ResidualGRUNet.npy)

The blender pyhton scripts are available in the [dir](/Batch_render_Blender_scripts/) for automatically spawning Shapenet objects and generating a video which is shot from different views around the object.
## Installation

The package requires python3. You can follow the direction below to install virtual environment within the repository or install anaconda for python 3.

- Download the repository

```
git clone https://github.com/chrischoy/3D-R2N2.git
```

- Setup the anaconda virtual environment and installing requirements ([How to use anaconda](https://conda.io/docs/user-guide/install/index.html))

```
cd 3D-R2N2
conda create -n py3-theano python=3.6
source activate py3-theano
conda install pygpu
pip install -r requirements.txt
```
- copy the theanorc file to the `$HOME` directory

```
cp .theanorc ~/.theanorc
```


### Running demo.py

- Install meshlab (skip if you have another mesh viewer). If you skip this step, demo code will not visualize the final prediction.

```
sudo apt-get install meshlab
```

- Run the demo code and save the final 3D reconstruction to a mesh file named `prediction.obj`

```
python demo.py prediction.obj
```

The demo code takes 3 images of the same chair and generates the following reconstruction.

| Image 1         | Image 2         | Image 3         | Reconstruction                                                                            |
|:---------------:|:---------------:|:---------------:|:-----------------------------------------------------------------------------------------:|
| ![](imgs/0.png) | ![](imgs/1.png) | ![](imgs/2.png) | <img src="https://github.com/chrischoy/3D-R2N2/blob/master/imgs/pred.png" height="127px"> |

- Deactivate your environment when you are done

```
deactivate
```


### Training the network

- Activate the virtual environment before you run the experiments.

```
source py3/bin/activate
```

- Download datasets and place them in a folder named `ShapeNet`

```
mkdir ShapeNet/
wget http://cvgl.stanford.edu/data2/ShapeNetRendering.tgz
wget http://cvgl.stanford.edu/data2/ShapeNetVox32.tgz
tar -xzf ShapeNetRendering.tgz -C ShapeNet/
tar -xzf ShapeNetVox32.tgz -C ShapeNet/
```

- Train and test the network using the training shell script

```
./experiments/script/res_gru_net.sh
```

**Note**: The initial compilation might take awhile if you run the theano for the first time due to various compilations. The problem will not persist for the subsequent runs.


## Using cuDNN

To use `cuDNN` library, you have to download `cuDNN` from the nvidia [website](https://developer.nvidia.com/rdp/cudnn-download). Then, extract the files to any directory and append the directory to the environment variables like the following. Please replace the `/path/to/cuDNN/` to the directory that you extracted `cuDNN`.

```
export LD_LIBRARY_PATH=/path/to/cuDNN/lib64:$LD_LIBRARY_PATH
export CPATH=/path/to/cuDNN/include:$CPATH
export LIBRARY_PATH=/path/to/cuDNN/lib64:$LD_LIBRARY_PATH
```

For more details, please refer to [http://deeplearning.net/software/theano/library/sandbox/cuda/dnn.html](http://deeplearning.net/software/theano/library/sandbox/cuda/dnn.html)


## Follow-up Paper

Gwak et al., [Weakly supervised 3D Reconstruction with Adversarial Constraint](https://arxiv.org/abs/1705.10904), [project website](http://cvgl.stanford.edu/mcrecon/)

