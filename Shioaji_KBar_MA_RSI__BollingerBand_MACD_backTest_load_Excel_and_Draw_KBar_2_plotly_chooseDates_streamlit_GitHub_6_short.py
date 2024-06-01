# 載入必要模組
import os
# os.chdir(r'C:\Users\user\Dropbox\系務\專題實作\112\金融看板\for students')
#import haohaninfo
#from order_Lo8 import Record
import numpy as np
#from talib.abstract import SMA,EMA, WMA, RSI, BBANDS, MACD
#import sys
import indicator_f_Lo2_short,datetime, indicator_forKBar_short
import datetime
import pandas as pd
import streamlit as st 
import streamlit.components.v1 as stc 


###### (1) 開始設定 ######
html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">金融資料視覺化呈現 (金融看板) </h1>
		<h2 style="color:white;text-align:center;">Financial Dashboard </h2>
		</div>
                <div class="grid-item">
                    <h2>Subtitle 2</h2>
                    <p>Content for subtitle 2.</p>
                </div>
                <div class="grid-item">
                    <h2>Subtitle 3</h2>
                    <p>Content for subtitle 3.</p>
                </div>
                <div class="grid-item">
                    <h2>Subtitle 4</h2>
                    <p>Content for subtitle 4.</p>
                </div>
		"""
stc.html(html_temp)












