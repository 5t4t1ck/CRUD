from setuptools import setup

setup(
    name="mn",
    version="0.1",
    py_modules=["mn"],
    install_requires=[
        "Click",
    ],
    entry_points="""
    [console_scripts]
    mn=mn:cli
    """,
)