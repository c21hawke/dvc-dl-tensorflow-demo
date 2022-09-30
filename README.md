# DVC - DL - TF - DEMO

download data --> [source](link)

## Commands

### create a new enc
```bash
source activate ./env
```

### init dvc
```bash
git init
dvc init
```

### create empty files -
```bash
mkdir -p src/utils config
touch src/__init__.py src/utils/__init__.py params.yaml dvc.yaml config/config.yaml src/stage_01_load_save.py src/utils/all_utils.py setup.py .gitignore
```

### install src
```bash
pip install -e .
```
