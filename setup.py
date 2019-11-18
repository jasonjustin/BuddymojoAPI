import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="buddymojoAPI",  # Replace with your own username
    version="1.0.10",
    author="Jelly Hsu",
    author_email="zxc3.zxc46@gmail.com",
    description="An API of cn.buddymojo.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jasonjustin/BuddymojoAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests', 'argparse']
)
