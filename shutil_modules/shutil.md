# 概述
> shutil模块提供了基于文件和文件夹的更高维度的操作，例如复制和移除等等

# 文件操作
## shutil.copyfile(src,dst,follow_symlinks=True)
> 复制一个文件

```
# dst也必须是一个文件名.
shutil.copyfile('D://new_folder2/test2/testsample.txt',"D://new_folder2//testsample.txt")
```
## shutil.copy(src,dst,follow_symlinks=True)
> 针对文件，复制操作

```
shutil.copy('D://new_folder2//test2//testsample.txt',"D://new_folder2//testsample2.txt")
```

## shutil.copy2(src,dst,follow_symlinks=True)
> 类似copy，不同的是，这个copy会同样复制文件的元数据。元数据指的是一个文件的权限，大小，创建时间等等。

## shutil.copytree(src,dst)
```
shutil.copytree(src, dst, symlinks=False, ignore=None,copy_function=copy2, ignore_dangling_symlinks=False)
```
> 复制文件夹,底下的文件，文件夹都会被复制。

```
shutil.copytree('D://new_folder2//test2',"D://new_folder2//test222",copy_function=shutil.copy2)

```
## shutil.rmtree(path)
> 移除文件夹及底下的文件

```
shutil.rmtree("D://new_folder2//test222")
```

## shutil.move(src,dst,copy_function=copy2)
> 递归移动一个文件或者文件夹到dst，然后返回路径

```
shutil.move('D://new_folder2/test3','D://new_folder2/test4')

>>>>返回D://new_folder2/test4\test2

```

## shutil.disk_usage(path)
> 返回以bytes为单位的磁盘使用情况

```
print(shutil.disk_usage('D://'))
>>>> usage(total=84001771520, used=76966387712, free=7035383808)

```

## shutil.chown(path,user=None,group=None)
> 改变一个文件/文件夹的所有者

```
shutil.chown(path,user,group)
```

## shutil.which(cmd)
> 显示可执行程序所在的路径
```
shutil.which('python')
```
# 归档压缩操作
## shutil.make_archive(basename,format,root_dir,base_dir)
```
basename: 要创建的压缩文件名，需要包含路径
format： zip,tar,gztar,bztar,zxtar
root_dir: 先进去这个root_dir的目录，然后在压缩base_dir的所有东西
base_dir: 路径的前缀

shutil.make_archive("D://new_folder2/test3",'zip','D://new_folder2/','D://new_folder2/test3')

```
## shutil.unpack_archive(filename,extract_dir,format)
> 解压缩
```
# test1 不存在，但是会自动创建
shutil.unpack_archive('D://new_folder2/test3.zip',"D://new_folder2//test1","zip")
```