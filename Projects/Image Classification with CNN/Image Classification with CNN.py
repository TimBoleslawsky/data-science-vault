import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms, models
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
import torch.nn.functional as F
import matplotlib.pyplot as plt
import time

# Defining Models 
class SimpleCNN(nn.Module):
    """
    This is our simple CNN that we use as a starting point. 
    """
    def __init__(self):
        super(SimpleCNN, self).__init__()

        # First conv block: input RGB (3) -> 16 feature maps
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.pool1 = nn.MaxPool2d(2, 2)  # First downsampling

        # Second conv block: 16 -> 32 feature maps
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.pool2 = nn.MaxPool2d(2, 2)  # Second downsampling

        # 128x128 images are 32x32 at this point
        self.fc1 = nn.Linear(32 * 32 * 32, 128)
        self.fc2 = nn.Linear(128, 2)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool1(x)

        x = F.relu(self.conv2(x))
        x = self.pool2(x)

        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

class BatchNCNN(nn.Module):
    """
    This is the first improvement upon our simple CNN.
    Here we introduce BatchNorm after each convolutional layer. 
    """
    def __init__(self):
        super(BatchNCNN, self).__init__()

        # First conv block: input RGB (3) -> 16 feature maps
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(16)
        self.pool1 = nn.MaxPool2d(2, 2)

        # Second conv block: 16 -> 32 feature maps
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(32)
        self.pool2 = nn.MaxPool2d(2, 2)

        # Fully connected layers
        self.fc1 = nn.Linear(32 * 32 * 32, 128)
        self.bn_fc = nn.BatchNorm1d(128) 
        self.fc2 = nn.Linear(128, 2)

    def forward(self, x):
        x = self.pool1(F.relu(self.bn1(self.conv1(x))))
        x = self.pool2(F.relu(self.bn2(self.conv2(x))))

        x = torch.flatten(x, 1)
        x = F.relu(self.bn_fc(self.fc1(x)))  
        x = self.fc2(x)
        return x

class AdvancedBatchNCNN(nn.Module):
    """
    This is an advanced version of the BatchCNN. 
    We use this model to experiment with different numbers of layers.
    """
    def __init__(self):
        super(AdvancedBatchNCNN, self).__init__()

        # Block 1: input 3 -> 16 channels
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(16)
        self.pool1 = nn.MaxPool2d(2, 2)  # 128 -> 64

        # Block 2: 16 -> 32 channels
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(32)
        self.pool2 = nn.MaxPool2d(2, 2)  # 64 -> 32

        # Block 3: 32 -> 64 channels
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm2d(64)
        self.pool3 = nn.MaxPool2d(2, 2)  # 32 -> 16

        # Block 4: 64 -> 128 channels
        self.conv4 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.bn4 = nn.BatchNorm2d(128)
        self.pool4 = nn.MaxPool2d(2, 2)  # 16 -> 8

        # Fully connected layers
        self.fc1 = nn.Linear(128 * 8 * 8, 128)
        self.bn_fc = nn.BatchNorm1d(128)
        self.fc2 = nn.Linear(128, 2)

    def forward(self, x):
        x = self.pool1(F.relu(self.bn1(self.conv1(x))))
        x = self.pool2(F.relu(self.bn2(self.conv2(x))))
        x = self.pool3(F.relu(self.bn3(self.conv3(x))))
        x = self.pool4(F.relu(self.bn4(self.conv4(x))))

        x = torch.flatten(x, 1)
        x = F.relu(self.bn_fc(self.fc1(x)))
        x = self.fc2(x)
        return x

class ResidualCNN(nn.Module):
    """
    This is the implementation of the AdvancedBatchCNN with residual blocks. 
    We omit the implementation of the BatchCnn with the residual blocks, 
    because it showed no improvement in the accuracy and because it looks
    very similar to this implementation. 
    """
    def __init__(self):
        super(ResidualCNN, self).__init__()

        # Input: [3, 128, 128] → Conv → [16, 128, 128]
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True)
        )
        self.pool1 = nn.MaxPool2d(2, 2)  # → [16, 64, 64]

        # Conv to expand channels from 16 → 32, then residual block
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.res2 = ResidualBlock(32)
        self.pool2 = nn.MaxPool2d(2, 2)  # → [32, 32, 32]

        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.res3 = ResidualBlock(64)
        self.pool3 = nn.MaxPool2d(2, 2)  # → [64, 16, 16]

        self.conv4 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.res4 = ResidualBlock(128)
        self.pool4 = nn.MaxPool2d(2, 2)  # → [128, 8, 8]

        # Flattened shape: 128 * 8 * 8 = 8192
        self.fc1 = nn.Linear(128 * 8 * 8, 128)
        self.bn_fc = nn.BatchNorm1d(128)
        self.fc2 = nn.Linear(128, 2)

    def forward(self, x):
        x = self.pool1(self.block1(x))      # [16, 64, 64]
        x = self.pool2(self.res2(self.conv2(x)))  # [32, 32, 32]
        x = self.pool3(self.res3(self.conv3(x)))  # [64, 16, 16]
        x = self.pool4(self.res4(self.conv4(x)))  # [128, 8, 8]

        x = torch.flatten(x, 1)
        x = F.relu(self.bn_fc(self.fc1(x)))
        x = self.fc2(x)
        return x
    
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(channels, channels, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.relu = nn.ReLU(inplace=True)

        self.conv2 = nn.Conv2d(channels, channels, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)

    def forward(self, x):
        identity = x
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += identity
        out = self.relu(out)
        return out

# Define Training
def train(model, train_loader):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * inputs.size(0)  
        _, predicted = torch.max(outputs, 1)
        correct += (predicted == labels).sum().item()
        total += labels.size(0)

    avg_loss = running_loss / total
    accuracy = correct / total
    return accuracy, avg_loss

# Define Evaluation
def evaluate(model, loader):
    model.eval()
    total = 0
    correct = 0
    with torch.no_grad():
        for inputs, labels in loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()
    return correct / total

if __name__ == '__main__':
    # Transfer learning
    weights_id = models.VGG16_Weights.IMAGENET1K_V1
    vggmodel = models.vgg16(weights=weights_id)
    vggmodel.eval()
    vggtransforms = weights_id.transforms()

    for param in vggmodel.parameters():
        param.requires_grad = False # Freezing parameters

    vggmodel.classifier[6] = nn.Linear(in_features=4096, out_features=2) # Set two classes

    # Defining Transformation
    transform_train = transforms.Compose([
        transforms.RandomHorizontalFlip(), # Added for data augmentation   
        transforms.RandomRotation(15), # Added for data augmentation   
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2), # Added for data augmentation               
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5], std=[0.5])       
    ])

    transform_val = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5], std=[0.5])
    ])

    transform_vgg_train = vggtransforms # This is for transfer learning
    transform_vgg_val = vggtransforms # This is for transfer learning

    # ImageFolder locates and formats the data 
    train_set = ImageFolder('a5_data_new/train', transform=transform_train)
    val_set = ImageFolder('a5_data_new/val', transform=transform_val)
    test_set = ImageFolder('a5_data_test/test', transform=transform_val)

    # DataLoader delivers it efficiently to the model
    train_loader = DataLoader(train_set, batch_size=8, shuffle=True, num_workers=4)
    val_loader = DataLoader(val_set, batch_size=8, shuffle=False, num_workers=4)
    test_loader = DataLoader(test_set, batch_size=8, shuffle=False, num_workers=4)

    # Define Training
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = AdvancedBatchNCNN().to(device) # Changed the model here
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)               

    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.5) # halves the learning rate every 3 epochs.

    # Training Loop 
    best_val_acc = 0.0
    patience = 3
    epochs_no_improve = 0
    early_stop = False

    total_time = 0
    num_epochs = 30

    for epoch in range(num_epochs):
        if early_stop:
            print(f"\nEarly stopping at epoch {epoch+1}")
            break

        start = time.time()

        train_acc, train_loss = train(model, train_loader)
        val_acc = evaluate(model, val_loader)

        scheduler.step()

        # Early Stopping Check
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            epochs_no_improve = 0
            torch.save(model.state_dict(), 'best_model.pth') # Save best model for testing on test set
        else:
            epochs_no_improve += 1
            if epochs_no_improve >= patience:
                early_stop = True

        end = time.time()
        epoch_time = end - start
        total_time += epoch_time

        print(f"Epoch {epoch+1}: Train Acc = {train_acc:.4f}, Train Loss = {train_loss:.4f}, "
            f"Val Acc = {val_acc:.4f}, Time = {epoch_time:.2f}s")

    avg_time = total_time / (epoch + 1)
    print(f"\nAverage training time per epoch: {avg_time:.2f} seconds")
    print(f"Best validation accuracy: {best_val_acc:.4f}")

    # Test model on test set
    model.load_state_dict(torch.load('best_model.pth'))
    model.eval()

    test_acc = evaluate(model, test_loader)
    print(f"Test Accuracy: {test_acc:.4f}")
