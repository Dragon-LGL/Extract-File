# Extract-File
## 将指定文件夹下的指定格式文件提取（复制）到目标文件夹下

### 1.多线程介绍
``` 多线程并发复制文件到目标文件夹
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for file in file_list:
            future = executor.submit(shutil.copy, file, target_dir)
            futures.append(future)
        wait(futures, return_when=ALL_COMPLETED)
```
* 其中ThreadPoolExecutor是Python的线程池类，用来实现多线程并发处理任务。
* max_workers参数指定线程池的线程数。
* submit方法用来提交任务到线程池，这里使用shutil.copy函数复制文件。
* wait方法用来等待线程池中的所有任务执行完毕。

### 2.复制函数
```
    future = executor.submit(shutil.copy, file, target_dir)
```
这段代码使用了concurrent.futures模块中的Executor类和submit方法，并将shutil.copy函数作为参数传递给了submit方法，表示要使用多线程异步地执行shutil.copy函数，其中file是要复制的文件路径，target_dir是目标文件夹路径。

submit方法返回一个Future对象，它代表一个未完成的任务。我们可以通过Future对象来获取任务的执行状态和结果。在这里，future是一个Future对象，代表了复制任务的执行状态和结果。





