import shutil
import os


#如果取原文件名作为新文件名的话，由于原文件名有重复，会导致覆盖，故需要取多层路径
#取多层路径还需要创建多层路径，改用最简单的方式，数字作为名字
'''
def get_new_name(new_name_list):
    for i in range(4):
        new_name_list.pop(0);
    filename = "\\".join(new_name_list);
    return filename;


def main():
    with open("upload.efu", "r") as f_r:
        lines = f_r.readlines();
        lines.pop(0);
        #print(lines);
        for line in lines:
            line_list = line.split(",");
            #print(line_list[0]);
            srcFile = line_list[0].strip('"');
            print(srcFile);
            new_name_list = srcFile.split("\\");
            filename = get_new_name(new_name_list)
            print(filename);
            dstFile = "C:\\Users\\ybdt\\Desktop\\upload\\" + filename;
            shutil.copyfile(srcFile, dstFile);
'''


def main():
    with open("upload.efu", "r") as f_r:
        lines = f_r.readlines();
        lines.pop(0);
        #print(lines);
        count = 1;
        for line in lines:
            line_list = line.split(",");
            #print(line_list[0]);
            srcFile = line_list[0].strip('"');
            print(srcFile);
            dstFile = "C:\\Users\\ybdt\\Desktop\\upload\\" + str(count) + ".php";
            shutil.copyfile(srcFile, dstFile);
            count += 1;


main();