from setuptools import setup


setup(
    name = 'todo_catalog',
    version = '0.1.3',
    py_modules = ['todo_catalog'],
    install_requires = [
        'Click',
        'os',
        'sys',
        're'
    ],
    entry_points = '''
        [console_scripts]
        todo_catalog=todo_catalog:find_todos
    '''
)
