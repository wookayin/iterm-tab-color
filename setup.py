from setuptools import setup

__version__ = '0.3.0'

install_requires = [
]

tests_requires = [
]

setup(
    name='iterm-tab-color',
    version=__version__,
    license='MIT',
    description="Change iTerm2's tab color",
    url='https://github.com/wookayin/iterm-tab-color',
    author='Jongwook Choi',
    author_email='wookayin@gmail.com',
    keywords='iterm iterm2',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    install_requires=install_requires,
    extras_require={'test': tests_requires},
    tests_require=tests_requires,
    scripts=['iterm-tab-color'],
    include_package_data=True,
    zip_safe=False,
)
