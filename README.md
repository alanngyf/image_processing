# project setup

## create virtual env, and install relevant packages
- conda create -n image_processing_main python=3.12
- conda activate image_processing_main
- nvcc --version

- pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
- pip install matplotlib
- pip install pandas
- pip install tqdm
- pip install flask
- pip install scikit-learn
- pip install jupyter

## activate and select the image_processing_main env for the project
conda activate image_processing

## deactivate the env
conda deactivate image_processing_main
