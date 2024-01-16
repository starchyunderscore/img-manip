from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('main.py', base=base, target_name = 'img-manip')
]

setup(name='img-manip',
      version = '1.0',
      description = 'image manipulation',
      options = {'build_exe': build_options},
      executables = executables)
