import wandb

print(f"THe version of wandb is: {wandb.__version__}")
assert wandb.__version__ == '0.14.2', f'Expected version 0.14.2, but got {wandb.__version__}'