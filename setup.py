import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Light Projects Generator",
    version="0.0.4",
    author="Philentropy",
    author_email="weltrusten@philentropy.org",
    description="Light Projects Generator is a simple web projects generator supporting Flutter, Symfony and React.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/w3lt3rust3n/light-projects-generator",
    project_urls={
        "Bug Tracker": "https://github.com/w3lt3rust3n/light-projects-generator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL",
        "Operating System :: Linux",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)