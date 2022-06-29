from torch.optim.lr_scheduler import _LRScheduler


class WarmUpLR(_LRScheduler):

    def __init__(self, optimizer, total_iterations, last_epoch=-1):
        self.total_iterations = total_iterations
        super().__init__(optimizer, last_epoch)

    def get_lr(self):
        return [base_lr * self.last_epoch / (self.total_iterations + 1e-8) for base_lr in self.base_lrs]