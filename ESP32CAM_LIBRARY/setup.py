from setuptools import setup, find_packages

setup(
    name="ESP32CAMWEB",
    version="1.0.0",
    author="Ruben Sahuquillo Redondo",
    author_email="rsahuquillo.ingeniero@gmail.com",
    description="Python library to control ESP32-CAM modules via HTTP requests",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu_usuario/ESP32CAM_LIBRARY",
    packages=find_packages(),
    package_dir={"": "ESP32CAMWEB"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Creative Commons Attribution 4.0 International",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["requests","numpy"],
)
