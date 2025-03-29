from setuptools import setup, find_packages

setup(
    name="DummyUIApp",
    version="0.1.0",
    author="Nickolas Whitman",
    description="Example Commanding UI Application.",
    long_description=open("README.md", encoding="utf-8").read(),
    url="https://github.com/NickolasDesigns/CICDPipelineProjects.git",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
