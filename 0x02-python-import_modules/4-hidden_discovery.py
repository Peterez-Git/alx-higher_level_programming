#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_func = dir()
    for i in range(1, len(all_func)):
        if all_func[i][:2] != "__":
            print("{}".format(all_func[i]))
