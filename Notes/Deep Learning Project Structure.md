Below is my preferred project structure when doing any deep learning tasks. The core of this structure is to utilize the capabilities of PyTorch and PyTorch Lightning.
## Recommended PyTorch + Lightning Project Structure

```
project/
├── configs/
│   └── experiment_config.yaml  # hyperparameters & experiment setup
│
├── data/ - should be excluded from git!
│   ├── raw/                    # original, immutable data
│   ├── processed/              # offline-preprocessed data
│
├── datamodules/
│   └── dataset_name.py         # PyTorch Dataset + LightningDataModule
│
├── models/
│   └── model_name.py           # LightningModule (model + loss + optimizers)
│
├── reports/
│   └── reports.pdf             # Summarized findings of the experiments.
│
├── results/ - should be excluded from git!
│   └── modelname_taskname/     # Results organized by e.g. model and task.
│       └── version_0/          # Specific results for a run. 
│       └── ...
│
├── scripts/
│   └── preprocess_data.py           # Offline preprocessing (optional).
│   └── train_model.py          # Model training script.
│
└── utils/
│   └── helpers.py              # metrics, transforms, small utilities.
│
├── .gitignore
├── pyproject.toml
├── README.md
```

### Detailed Explanation of The Project Structure
I want to give a short justification and explanation of the above depicted project structure. This is based on common consensus and experience. 

**Configs:**
=> Configs should be structured as .yaml files. Here we can give command line arguments to the main scripts of the project in an orderly fashion. Example arguments: Model name, data to use, preprocessing steps, ...

**Data:**
=> The data should be structured as *raw* and *processed*, if we plan to do some offline processing within the project. If we already have the data preprocessed or can access the preprocessed data externally (e.g. some database), we can omit or simplify this folder.

**Datamodules:**
=> Here we want to use PyTorch Datasets and LightningDataModules to define how the data should be handle within the train pipeline. Importantly, we do not define a separate preprocessing step here. We can define splitting, normalization, etc., but all this happens online within the training pipeline. If we need any larger offline processing, we should not do this here, but in a separate script. 

The PyTorch Dataset defines how a single data point is fetched. We can either do this by creating our own dataset class that inherits from `Dataset` imported from `torch.utils.data`, or by using a predefined PyTorch Dataset class like `ImageFolder` imported from `torchvision.datasets`. This is then wrapped by a LightningModule. The LightningModule returns the Dataloaders used by the training pipeline and handles splitting, simple normalization, and so on. 

**Reports:**
=> This should contain findings that we find noteworthy and want to display to a wider audience. Usually this would summarize the experiments and their results. 

**Results:**
=> Here the specific results of training/ evaluation runs are stored. This should be configured using the `TensorBoardLogger` or the `CSVLogger` from `pytorch_lightning.loggers`. These are predefined loggers that let us view the results either in a TensorBoard application (opened in a browser) or a CSV file. 

**Scripts:**
=> Usually we would only have two scripts: train_model.py (always) and preprocess_data.py (if we need an offline preprocessor).
### Recommended Setup
The recommended `pyproject.toml` boilerplate to use with uv or poetry is shown below: 

```
[project]  
name = "project-name"  
version = "0.1.0"  
description = ""  
readme = "README.md"  
requires-python = ">=3.12,<3.14"  
authors = [{ name = "Name", email = "Mail" }]  
dependencies = [  
    "pytorch-lightning>=2.6.0",  
    "pyyaml>=6.0.3",  
    "tensorboard>=2.20.0",  
    "torch>=2.9.1",  
    "torchvision>=0.24.1",  
]
```

The recommended `.gitignore` setup is as follows: 

```
# Secrets & local env  
.env  
  
# Virtual environments  
.venv/  
venv/  
uv.lock  
  
# Python cache/bytecode  
__pycache__/  
*.py[cod]  
*.pyo  
*.pyd  
  
# Editors/IDEs  
.idea/  
.vscode/  
  
# Results  
results/  
  
# Data (too large for git)  
data/
```