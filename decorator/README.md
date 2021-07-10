Title: Python decorator應用與分享
Description: python可將function當成參數傳遞，python decorator可以利用此特性將要執行個功能在包覆上令一層功能。
Authors: GGFU
Date: 09/07/2021
Tags: 
ID: python_deco
base_url: https://ggfu0114.github.io/

# Python decorator

> 什麼時機點我需要用到python decorator?

如果在執行很多function之前都需要進行相同的操作，例如：驗證使用者身份，檢查傳入參數的型態...然後發現寫程式碼都是一直複製貼上時，就該司考試不是要把這些相同的操作寫成python decorator.


> Python decorator重要的概念
1. Decorator可將原本的function取代成其他的function.
2. 每當寫有decorator的module被載入時，decorator的function會立刻被執行一次.

> Python裡面標準的decorator library.
1. `lru_cache`: 利用decorator完成cache的功能，紀錄輸入的參數與回傳結果，當輸入參數相符，可直接回傳結果。
2. `singledispatch`: 類似if判斷式，但是可以利用register去處理不同的input參數type，而不需要一直修改if判斷式。

