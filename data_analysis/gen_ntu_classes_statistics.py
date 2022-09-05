import argparse
import os

import numpy as np
import pandas as pd

NUMBER_OF_CLASSES = 60


def get_parser():
    argument_parser = argparse.ArgumentParser(description="NTU-RGB-D Data Analyzer.")
    argument_parser.add_argument("--data_path", default="data/nturgbd_raw/skeletons")
    argument_parser.add_argument(
        "--ignored_sample_path",
        default="data/nturgbd_raw/NTU_RGBD_samples_with_missing_skeletons.txt",
    )
    argument_parser.add_argument(
        "--out_file_path", default="data_analysis/classes_statistics.csv"
    )
    return argument_parser


def init_action_classes_statistics_structure():
    statistics_structure = pd.DataFrame(
        {
            "number_of_samples": pd.Series(
                data=np.zeros(NUMBER_OF_CLASSES),
                index=np.arange(1, NUMBER_OF_CLASSES + 1),
                dtype=int,
            ),
        }
    )
    statistics_structure.index.name = "action_class"
    return statistics_structure


def create_ignored_samples_list(arg):
    if arg.ignored_sample_path != None:
        with open(arg.ignored_sample_path, "r") as f:
            ignored_samples = [line.strip() + ".skeleton" for line in f.readlines()]
    else:
        ignored_samples = []
    return ignored_samples


if __name__ == "__main__":
    parser = get_parser()
    arg = parser.parse_args()

    statistics = init_action_classes_statistics_structure()
    ignored_samples = create_ignored_samples_list(arg)

    for filename in os.listdir(arg.data_path):
        if filename in ignored_samples:
            continue
        action_class = int(filename[filename.find("A") + 1 : filename.find("A") + 4])
        statistics.at[action_class, "number_of_samples"] += 1
    
    statistics.to_csv(arg.out_file_path)
