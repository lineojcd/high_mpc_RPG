## Policy Search for Model Predictive Control with Application to Agile Drone Flight

### Req
Install ffmpeg
```
conda install -c conda-forge ffmpeg
```
Comple the c file for 64 bit arch
```
gcc -shared -o mpc_v1.so mpc_v1.c
```
### Installation

Clone the repo

```
git clone git@github.com:uzh-rpg/high_mpc.git
```

Installation Dependencies:

```
cd high_mpc
pip install -r requirements.txt
```

Add the repo path to your PYTHONPATH by adding the following to your ~/.bashrc

```
export PYTHONPATH=${PYTHONPATH}:/path/to/high_mpc
```

### Run

Standard MPC

```
cd high_mpc
python3 run_mpc.py
```

Learning a High-Level Policy

```
python3 run_highmpc.py
```

Learning a Deep High-Level Policy

```
# collect training data for the MLP
python3 run_deep_highmpc.py --option 0

# train the deep high-level policy with pre-collected data
python3 run_deep_highmpc.py --option 1

# evaluate the performance with pre-trained deep high-level policy
python3 run_deep_highmpc.py --option 2
```




### Publication

If you use this code in a publication, please cite the following papers:

Y. Song and D. Scaramuzza,
"**Policy Search for Model Predictive Control with Application to Agile Drone Flight**,"
IEEE Transaction on Robotics (T-RO), 2021.
[[PDF](http://rpg.ifi.uzh.ch/docs/TRO21_Yunlong.pdf)][[Video](https://youtu.be/Qei7oGiEIxY)]

Y. Song and D. Scaramuzza,
"**Learning High-Level Policies for Model Predictive Control**,"
IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Las Vegas, 2020.
[[PDF](http://rpg.ifi.uzh.ch/docs/IROS20_Yunlong.pdf)][[Video](https://youtu.be/2uQcRnp7yI0)]

```
@article{song2022policy,  
  author={Song, Yunlong and Scaramuzza, Davide},  
  journal={IEEE Transactions on Robotics},   
  title={Policy Search for Model Predictive Control With Application to Agile Drone Flight},   
  year={2022}, 
  pages={1-17},  
  doi={10.1109/TRO.2022.3141602}
}
```
```
@inProceedings{song2020learning,
  title={Learning High-Level Policies for Model Predictive Control},
  author={Song, Yunlong and Scaramuzza, Davide},
  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  year={2020}
}
```
