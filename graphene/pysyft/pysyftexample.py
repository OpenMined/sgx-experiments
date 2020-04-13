import torch
import syft as sy
from torch import nn, optim

hook = sy.TorchHook(torch)

# create a couple workers

bob = sy.VirtualWorker(hook, id="bob")
alice = sy.VirtualWorker(hook, id="alice")
secure_worker = sy.VirtualWorker(hook, id="secure_worker")


# A Toy Dataset
data = torch.tensor([[0,0],[0,1],[1,0],[1,1.]], requires_grad=True)
target = torch.tensor([[0],[0],[1],[1.]], requires_grad=True)

# get pointers to training data on each worker by
# sending some training data to bob and alice
bobs_data = data[0:2].send(bob)
bobs_target = target[0:2].send(bob)

alices_data = data[2:].send(alice)
alices_target = target[2:].send(alice)

# Iniitalize A Toy Model
model = nn.Linear(2,1)

iterations = 10
worker_iters = 5

for a_iter in range(iterations):
    
    bobs_model = model.copy().send(bob)
    alices_model = model.copy().send(alice)

    bobs_opt = optim.SGD(params=bobs_model.parameters(),lr=0.1)
    alices_opt = optim.SGD(params=alices_model.parameters(),lr=0.1)

    for wi in range(worker_iters):

        # Train Bob's Model
        bobs_opt.zero_grad()
        bobs_pred = bobs_model(bobs_data)
        bobs_loss = ((bobs_pred - bobs_target)**2).sum()
        bobs_loss.backward()

        bobs_opt.step()
        bobs_loss = bobs_loss.get().data

        # Train Alice's Model
        alices_opt.zero_grad()
        alices_pred = alices_model(alices_data)
        alices_loss = ((alices_pred - alices_target)**2).sum()
        alices_loss.backward()

        alices_opt.step()
        alices_loss = alices_loss.get().data
    
    alices_model.move(secure_worker)
    bobs_model.move(secure_worker)
    with torch.no_grad():
        model.weight.set_(((alices_model.weight.data + bobs_model.weight.data) / 2).get())
        model.bias.set_(((alices_model.bias.data + bobs_model.bias.data) / 2).get())
    
    print("Bob:" + str(bobs_loss) + " Alice:" + str(alices_loss))

preds = model(data)
loss = ((preds - target) ** 2).sum()

print(preds)
print(target)
print(loss.data)