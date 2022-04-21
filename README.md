# S-Class Scraping Tool

## Description
Tool for scraping lesson data from S-Class.

## Requirements

- Python 3.x
- Selenimu 
- Google Chrome
- Google Chrome Driver
- GUI environment (Does not run in CLI environment)

## How to Use
In this case I'm using Anaconda.
1. Download [Chrome Driver](https://chromedriver.chromium.org/downloads).
2. Unzip in Scraping/
3. Create virtual environment and install selenium.
    ```bash
    conda create --name hogehoge python=3.8
    conda activate hogehoge
    pip install selenium
    ```
4. Run scraping. class.json will be created.
    ```bash
    python scraping.py
    ```
5. Deactivate virtual environment.
    ```bash
    conda deactivate hogehoge
    ```
6. Remove virtual environment (option).
    ```bash
    conda remove hogehoge --all
    ```

## Technology we use
<p align="left"> 
  <a href="https://www.python.org/"><img alt="Python" height="64px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/165px-Python-logo-notext.svg.png" /></a>　
  <a href="https://www.selenium.dev/"><img alt="selenium" height="64px" src="https://www.selenium.dev/images/logos/webdriver.svg" /></a>
</p>

## Featured In 
<p>
    <a href="https://suwageekes.github.io/HomePage/">
    <img alt="org_logo" height="64px" src="https://avatars.githubusercontent.com/u/102970678?s=200&v=4" /></a>
</p>

