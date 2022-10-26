import setuptools

setuptools.setup(
    name="tiny_queue",
    version="0.0.1",
    author="",
    author_email="",
    description="",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=["tiny_queue","tiny_queue.connections"],
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "sqlitedict == 2.0.0",
        "appdirs == 1.4.4",
        "fire == 0.4.0",
        "filelock == 3.8.0",
        "loguru == 0.6.0",
        "cryptography==37.0.1",
        "redis-dict==1.6.0",
        "python-redis-lock==4.0.0",
    ],
    
    entry_points={"console_scripts": ["tiny_queue = tiny_queue.cli:main"]},

)
