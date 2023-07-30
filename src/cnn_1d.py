import optuna
import torch
import torch.optim as optim
from optuna.trial import TrialState
from sklearn.preprocessing import StandardScaler
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torchsummary import summary
from torchvision import datasets, transforms
from torchvision.transforms import ToTensor


class ConvolutionalNeuralNetwork(nn.Module):
    def __init__(
        self,
        trial,
        num_filter_1,
        num_filter_2,
        num_filter_3,
        num_fc,
        drop_out_rate_1,
        drop_out_rate_2,
        drop_out_rate_3,
    ):
        """
        Parameters:
            - trial (optuna.trial._trial.Trial): Optuna trial
            - num_filters (int):                 Number of filters of conv layers
            - num_fc (int):                      Number of neurons of FC layers
            - drop_out_rate (float):             Dropout ratio
        """
        super(ConvolutionalNeuralNetwork, self).__init__()
        self.main = nn.Sequential(
            nn.Conv1d(8, num_filter_1, kernel_size=3, padding=1),  # num_filter_1, 24
            nn.ReLU(),
            nn.MaxPool1d(2),  # num_filter_1, 12
            nn.Dropout(drop_out_rate_1),
            nn.Conv1d(
                num_filter_1, num_filter_2, kernel_size=3, padding=1
            ),  # num_filter_2, 12
            nn.ReLU(),
            nn.MaxPool1d(2),  # num_filter_2,  6
            nn.Dropout(drop_out_rate_2),
            nn.Conv1d(
                num_filter_2, num_filter_3, kernel_size=3, padding=1
            ),  # num_filter_3, 6
            nn.ReLU(),
            nn.MaxPool1d(2),  # num_filter_3, 3
            nn.Dropout(drop_out_rate_3),
            nn.Flatten(),  # num_filter_3 x 3
            nn.Linear(num_filter_3 * 3, num_fc),  # num_fc
            nn.ReLU(),
            nn.Linear(num_fc, 1),
        )

    def forward(self, x):
        logits = self.main(x)
        return logits
    

    