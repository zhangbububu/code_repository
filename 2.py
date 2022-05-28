


import torch


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.l1 = torch.nn.Linear(4,16)
        self.l2 = torch.nn.Linear(16,2)



    def forward(self,x):
        x = (self.l2(self.l1(x)))
        return x


model = Net()
x = torch.randn(3,4)

print(x,'\n',model(x))

with torch.autograd.profiler.profile(enabled=True, use_cuda=True, record_shapes=True) as prof:
    outputs = model(x)
print(prof.table())

