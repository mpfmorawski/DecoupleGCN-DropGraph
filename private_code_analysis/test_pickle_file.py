import argparse
import pickle


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Testing pkl files')
    parser.add_argument('--file_path', default='data/ntu/xsub/train_label.pkl')

    arg = parser.parse_args()

    with open(arg.file_path, 'rb') as f:
        x = pickle.load(f)

    x

    '''
    x[0] - list of filenames
    x[1] - list of labels (action class numbers minus one) 
    
    Examples:
    x[0][0] == 'S008C001P034R002A036.skeleton'
    x[1][0] == 35
    '''
    