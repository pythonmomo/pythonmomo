import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythonmomo",
    version="0.0.1",
    author="Abulo John Joshua, Allan Guwatudde, Sserubiri william",
    author_email="john.abulo@andela.com, allan.guwatudde@andela.com",
    description="A simple to use python wrapper to integrate the MTN Uganda MoMoPay API into your projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pythonmomo/pythonmomo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)