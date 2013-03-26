skinator
========

Templatable file renderer.

Usage
-----

Put files in `base` directory, run `skinator.py` and voilá: the files will be copied to the `outputs` directory.

Of course skinator doesn't simply copy files. It'll check the variables declared in the `config/base_config.ini`, get the base files and creates a copy of them in the `outputs` directory with the placeholders replaced. To make it work, put placeholders in the base files in this format `{{name_of_declared_variable_in_config}}`

For further information, check the `config/base_config.ini`. It controls the variables and the name of the output directory.

You can declare your own config file. Just use the two sections (`folder_options` and `variables`). The only obligatory config is the `master_output_folder`, under `folder_options`. Other variables are up to you. After declaring your config file, when you run skinator, just pass the name of the file through command line (e.g. `skinator.py my_config_file`).
