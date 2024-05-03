from setuptools import setup, find_packages

setup(
    name='catman',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'catman=catman.cli:main',
        ],
    },
    install_requires=[
        'faiss-cpu==1.8.0',
        'numpy',
        'pillow',
        'torch==2.3.0',
        'torchvision',
        'transformers', 
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-mock',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
