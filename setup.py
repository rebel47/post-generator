"""
Setup script for Post Generator
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="linkedin-post-generator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A versatile LinkedIn-style post generator for creating branded social media content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rebel47/post-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Pillow>=10.0.0",
    ],
    extras_require={
        "api": [
            "fastapi>=0.104.0",
            "uvicorn>=0.24.0",
            "python-multipart>=0.0.6",
        ],
        "dev": [
            "black>=23.0.0",
            "pytest>=7.4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "post-generator=cli:main",
            "post-generator-batch=batch_generator:main",
        ],
    },
    include_package_data=True,
    package_data={
        "post_generator": ["*.json"],
    },
)
