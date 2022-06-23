import argparse
import sys

sys.path.append("./data_gen")
import ntu_gendata as ntu_gendata

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Testing read_xyz function')
    parser.add_argument('--file_path', default='data/nturgbd_raw/skeletons/S003C003P001R001A035.skeleton')

    arg = parser.parse_args()

    seq_info = ntu_gendata.read_skeleton_filter(arg.file_path)

    seq_info

    data = ntu_gendata.read_xyz(arg.file_path)

    data
    