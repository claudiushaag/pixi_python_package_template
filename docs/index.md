---
buttons:
  - title: Download Full Documentation (PDF)
    icon: fontawesome-regular-file-pdf
    attributes:
      href: documentation.pdf
---

# Pixi Python Template
[![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)

In order to use the different software-tools developed for this repo, the repo enables the software usage using the package manager [`Pixi`](https://pixi.sh/latest/).
It is a language-agnostic package manager, which makes use of the conda-package format.
It can easily be installed on any system and updated via
```
pixi self-update
```
To do so every now and then is encouraged, as the software is still in heavy development.
If the programm is installed, all the dependencies needed for the specific platform are installed and cached automatically.
When running any command or task, `pixi` first checks if the dependencies are up to date, and otherwise installs them.
The `pixi.lock` file documents all dependencies, their version and a hash for every usable platform, ensuring reliable reproducability.


## Pixi Tasks

These tasks are defined in the `pixi.toml` file and can be modified and inspected there.
Find out more on this feature [here](https://pixi.sh/latest/workspace/advanced_tasks/).

### List of currently defined tasks

{{ pixi_task_table() }}

Please note the need for arguments after some of the tasks.
Run the tasks by prepending "pixi run" before the taskname and appending any arguments:
```bash
pixi run <taskname> <arguments>
```


!!! info
    The usage of macros is shown by a [macro](mkdocs.md#using-macros), which automatically reads out the pixi tasks during creation of this documentation.