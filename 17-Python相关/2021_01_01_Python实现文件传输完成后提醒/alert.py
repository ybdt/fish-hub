#!/usr/bin/python3

import tkinter.messagebox
import os

def main():
    while(True):
        tasklist_obj = os.popen("tasklist");
        tasklist_content = tasklist_obj.read();
        if "scp"  in tasklist_content:
            sleep(3);
            continue;
        else:
            break;
    root = tkinter.Tk();
    root.withdraw();
    root.wm_attributes("-topmost", 1);
    tkinter.messagebox.showinfo("提示", "文件传输完毕，给裕哥发送过去");

main();
