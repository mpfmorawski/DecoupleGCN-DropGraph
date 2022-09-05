import argparse
import sys
import numpy as np

sys.path.append("./data_gen")
import preprocess as preprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Testing pre_normalization function')
    parser.add_argument('--file_path', default='test_scripts/data/ntu/xsub/train_data_joint_before_pre_normalization.npy')

    arg = parser.parse_args()

    data = np.load(arg.file_path)
    fp = preprocess.pre_normalization(data)

    fp
