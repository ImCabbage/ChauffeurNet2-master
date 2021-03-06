from network.train import ConfigSimpleConv
from simulator.UI.TestNetwork import Simulator
from simulator.UI.Record import Recorder
from download_data import check_if_data_exists
# opencv-python
# opencv-contrib-python
# numpy
# h5py
# matplotlib
# scipy
# torchvision

#if errors about opencv DLL
#https://github.com/skvark/opencv-python/issues/154
#https://www.microsoft.com/en-us/software-download/mediafeaturepack

#notes. when editing world. make sure that lanes are a plane object, make sure that they have a center, make sure to to export all
#TODO save .blend file somewhere with the world

def main():
    check_if_data_exists()

    record = False
    do_train = False
    just_test_network = True

    if record:
        recorder = Recorder(event_bag_path="data/recorded_states.pkl", world_path="data/world.obj")
        recorder.run()

    if do_train:
        cfg = ConfigSimpleConv(root_path=".")
        for epoch in range(cfg.epochs):
            cfg.train(epoch)

    if just_test_network:
        simulator = Simulator(event_bag_path="I:/project/ChauffeurNet-master/data/recorded_states.pkl", network_path="I:/project/ChauffeurNet-master/data/ChauffeurNet.pt" ,
                              world_path="I:/project/ChauffeurNet-master/data/world.obj",
                              to_video = False)

        simulator.run()


if __name__ =="__main__":
    main()