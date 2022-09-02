import argparse

import matplotlib.pyplot as plt
import pandas as pd


def get_parser():
    # parameter priority: command line > config > default
    argument_parser = argparse.ArgumentParser(
        description="Plots of loss and accuracy curves"
    )
    argument_parser.add_argument(
        "--filename",
        default="./postprocessing/statistics.csv",
    )
    return argument_parser

if __name__ == "__main__":
    parser = get_parser()
    arg = parser.parse_args()

    data = pd.read_csv(arg.filename)

    loss_curves = data.plot(x = 'epoch', y=['train_loss', 'eval_loss'], kind="line")
    loss_curves.figure.savefig("./postprocessing/loss_curve.png")

    accuracy_curves = data.plot(x = 'epoch', y=['train_accuracy', 'eval_accuracy'], kind="line")
    accuracy_curves.figure.savefig("./postprocessing/accuracy_curve.png")

