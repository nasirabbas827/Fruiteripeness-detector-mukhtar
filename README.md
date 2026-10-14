# Fruiteripeness Detector Mukhtar

Fruiteripeness-detector-mukhtar is an image-based fruit ripeness classification project.

![Tkinter](https://img.shields.io/badge/Tkinter-2563EB?style=flat-square)

## Overview

The Tkinter implementation is organized around the entry points and modules below.

## Implemented workflows

The source defines these handlers:

- **Create Gradient** — `create_gradient`
- **Predict Ripeness** — `predict_ripeness`

## Getting started

### 1. Get the project

```bash
git clone https://github.com/nasirabbas827/Fruiteripeness-detector-mukhtar.git
cd Fruiteripeness-detector-mukhtar
```

### 2. Prepare Python

Create an isolated environment:

```bash
python -m venv .venv
```

Activate it with `.venv\Scripts\activate` on Windows Command Prompt, or `source .venv/bin/activate` on macOS/Linux.

No requirements file is included. The inspected Python imports indicate these dependencies as a starting point:

```bash
python -m pip install Pillow numpy opencv-python tensorflow
```

Dependency versions are not pinned in this repository.

A working Tkinter installation and a graphical desktop session are required.

### 3. Configure and run

Run from the repository root so relative file paths resolve correctly:

```bash
python main.py
```

### Model files

Included artifacts: [`fruit_ripeness_cnn_model.h5`](fruit_ripeness_cnn_model.h5).

Keep models, preprocessing objects, and label mappings together in the locations expected by the source.

## Repository guide

| Path | Purpose |
| --- | --- |
| [`main.py`](main.py) | Application entry point |

## Development notes

These setup instructions are based on the repository source. The application has not been executed as part of this documentation update; verify dependencies and configuration in your local environment.
