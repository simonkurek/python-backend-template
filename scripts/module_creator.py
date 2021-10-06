import os

"""
Create __init__.py file in each subdirectory of project - creates submodules in project
Nessesery to project works
"""


class InitBuilder:

    def __init__(self):
        self.counter = 0

    def run(self):
        print('\n === generating __init__ files === \n')
        self.generate()
        print('\n === done === ')
        print(f': Created {self.counter} new files :\n')

    def generate(self, cur_dir=None):
        if cur_dir is None:
            cur_dir = os.getcwd()
        sub_dirs = os.listdir(cur_dir)
        for sub_dir in sub_dirs:
            if not os.path.isfile(sub_dir) and "." not in sub_dir:
                self.counter += 1
                sub_dir_path = os.path.join(cur_dir, sub_dir)
                init_file = os.path.join(sub_dir_path, "__init__.py")
                print(f'{init_file} created')
                #open(init_file, "w+")
                self.generate(sub_dir_path)


if __name__ == "__main__":
    init_builder = InitBuilder()
    init_builder.run()
