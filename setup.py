from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()
setup(
    name="open-data-platform",
    version="0.1.0",
    author="Tên của bạn",
    author_email="email@example.com",
    description="Nền tảng dữ liệu mở cho doanh nghiệp vừa và nhỏ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trangtoan293/open-data-platform",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "black>=21.5b1",
            "flake8>=3.9.0",
            "mypy>=0.812",
        ],
    },
    entry_points={
        "console_scripts": [
            "open-data-platform=open_data_platform.cli:main",
        ],
    },
)