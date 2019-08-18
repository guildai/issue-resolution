# Flag --save-trials not saving anything

https://github.com/guildai/guildai/issues/40

## Recreating issue

The problem can be recreated.

Requirements:

- guildai==0.6.5

Steps:

    $ cd issue-40
    $ guild run train \
        problem_train_size=[0.0002,0.0004,0.0008,0.0016,0.0032] \
        --save-trials mixup_semisupervised.csv

Guild shows:

    Saving 5 trial(s) to mixup_semisupervised.csv

However, the file `mixup_semisupervised.csv` is not created in the cwd.

    $ stat mixup_semisupervised.csv
    stat: cannot stat 'mixup_semisupervised.csv': No such file or directory

## Resolution

This was fixed with tests for 0.6.6 in
[35f44259](https://github.com/guildai/guildai/commit/35f442594737f46787ace6dbf9c3e5068483aab2).
