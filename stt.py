import time
from selenium import webdriver
from selenium.webdriver.common import keys
import time
from tkinter import *
from tkinter import messagebox
import webbrowser
import subprocess,json,time
import requests
import os
import ctypes   
from colorama import Fore, Back, Style
import socket
import sys
import smtplib, ssl
import ctypes, sys
from socket import gaierror
class Login:
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
    def login_fb(self,emails,passs):
        self.driver.get("https://traodoisub.com/")
        email = self.driver.find_element_by_id("username")
        pasw = self.driver.find_element_by_id("password")
        email.send_keys(emails)
        pasw.send_keys(passs)
        button = self.driver.find_element_by_id("loginclick")
        button.click()
        time.sleep(5)
        return self.driver
new_login = Login()
driver = new_login.login_fb("8EZ6Y19","daiyBeyfnF")
driver.get("https://traodoisub.com/")
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements_by_class_name("alert alert-danger alert-dismissible show")
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
