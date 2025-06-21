from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the contents of your requirements file
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="youtube_transcription_pipeline",
    version="1.0.0",
    author="Kunal Chhonkar", 
    author_email="chhonkar002ai@gmail.com",
    description="A pipeline to download and transcribe YouTube videos using a self-hosted Whisper model.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github", # Placeholder
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License", # Placeholder: Choose an appropriate license
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            # If you convert the notebook to a .py script, you can add a command-line entry point here.
            # 'transcribe=your_script_name:main',
        ],
    },
)