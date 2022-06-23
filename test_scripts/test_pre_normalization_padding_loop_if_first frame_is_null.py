import numpy as np

if __name__ == '__main__':
    person = np.array([
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],    # frame 0
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],    # frame 1
        [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],    # frame 2
        [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]],    # frame 3
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],    # frame 4
        [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]],    # frame 5
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]     # frame 6
        ])
    # person array size is (frames)x(joints)x(coords): 7x5x3


    if person[0].sum() == 0:
        # a = person.sum(-1)                    # a is an array of size 7 x 5 with sums of coords in joints
        # b = person.sum(-1).sum(-1)            # b is an array of size 7 with sums of all data in each frame
        index = (person.sum(-1).sum(-1) != 0)   # index is An array of size 7: [False, False, True, True, False, True, False]
        tmp = person[index].copy()              # tmp is an array of size 3x6x5 with frames in which data sum is not equal to zero
        person *= 0                             # Make every element in peson array equals to zero
        person[:len(tmp)] = tmp                 # Paste tmp array as first 3 frames in person aray

    person
    '''
    Output:
    Array with size 7x5x3
    which in comparison to init person array equals to:

    [frame2, frame3, frame5, nullframe, nullframe, nullframe, nullframe]
    
    where nullframe is frame which consists only of zeros. 
    '''