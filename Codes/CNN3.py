from __future__ import division, print_function
import sys
import torch
import torch.nn.init
import torch.nn as nn
import torch.optim as optim
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.autograd import Variable
import torch.backends.cudnn as cudnn
import torch.nn.functional as F
from Utils import L2Norm, cv2_scale, np_reshape


class DesNet(nn.Module):
    """DesdNet model definition
    """
    def __init__(self):
        super(DesNet, self).__init__()
        self.features = nn.Sequential(
            
            #CNN1
            nn.Conv2d(1, 32, kernel_size=3, stride=2, padding=1, bias = False),
            nn.BatchNorm2d(32, affine=False),
            nn.ReLU(),
            
            #CNN2
            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1, bias = False),
            nn.BatchNorm2d(64, affine=False),
            nn.ReLU(),
            
            #CNN3
            nn.Dropout(0.4),
            nn.Conv2d(64, 96, kernel_size=3, stride=2, padding=1, bias = False),
            nn.BatchNorm2d(96, affine=False),
            nn.ReLU(),
            
            #CNN3
            nn.Dropout(0.4),
            nn.Conv2d(96, 64, kernel_size=3, stride=1, padding=1, bias = False),
            nn.BatchNorm2d(64, affine=False),
            nn.ReLU(),
            
            #CNN2
            nn.Dropout(0.3),
            nn.Conv2d(64, 96, kernel_size=3, stride=1, padding=1, bias = False),
            nn.BatchNorm2d(96, affine=False),
            nn.ReLU(),

            #CNN1
            nn.Dropout(0.3),
            nn.Conv2d(96, 128, kernel_size=3, stride=1, padding=1, bias = False),
            nn.BatchNorm2d(128, affine=False),
            nn.ReLU(),

            #CNN1
            nn.Dropout(0.3),
            nn.Conv2d(128, 128, kernel_size=4, bias = False),
            nn.BatchNorm2d(128, affine=False),
        )
        self.features.apply(weights_init)
        return
    
    def input_norm(self,x):
        flat = x.view(x.size(0), -1)
        mp = torch.mean(flat, dim=1)
        sp = torch.std(flat, dim=1) + 1e-7
        return (x - mp.detach().unsqueeze(-1).unsqueeze(-1).unsqueeze(-1).expand_as(x)) / sp.detach().unsqueeze(-1).unsqueeze(-1).unsqueeze(1).expand_as(x)
    
    def forward(self, input):
        x_features = self.features(self.input_norm(input))
        x = x_features.view(x_features.size(0), -1)
        return L2Norm()(x)

    
def weights_init(m):
    if isinstance(m, nn.Conv2d):
        nn.init.orthogonal_(m.weight.data, gain=0.6)
        try:
            nn.init.constant(m.bias.data, 0.01)
        except:
            pass
    return