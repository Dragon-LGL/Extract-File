import os
import shutil
import threading
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


def copy_files(source_dir, target_dir, file_extension):
    """
    复制指定文件夹下指定格式文件到目标文件夹
    :param source_dir: 源文件夹路径
    :param target_dir: 目标文件夹路径
    :param file_extension: 文件格式（可以是后缀名或完整文件名）
    """
    # 获取指定文件夹下所有指定格式的文件名列表
    file_list = []
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            if filename.endswith(file_extension) or filename == file_extension:
                file_list.append(os.path.join(root, filename))

    # 多线程并发复制文件到目标文件夹
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for file in file_list:
            future = executor.submit(shutil.copy, file, target_dir)
            futures.append(future)
        wait(futures, return_when=ALL_COMPLETED)


if __name__ == '__main__':
    # 测试
    source_dir = r'E:\PS\data\人物'
    target_dir = r'E:\PS\data\123'
    file_extension = '.jpg'  # 指定格式可以是后缀名或完整文件名

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    copy_files(source_dir, target_dir, file_extension)
    print('复制完成！')
