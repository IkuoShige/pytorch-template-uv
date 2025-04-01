import torch
print("torch version: ")
print(torch.__version__)
print("torch available: ")
print(torch.cuda.is_available())
print("device name: ")
print(torch.cuda.get_device_name())

