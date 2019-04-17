# 介绍
这个小工具用于将字幕文件中的所有空行、段落号、时间戳去除。
# 教程
`python process.py 源文件路径 目标文件路径`
* 源文件路径——原始的字幕文件，里面有很多时间戳、空行、行号。
* 目标文件路径——新建一个文件，将处理后的数据保存到该文件中。

例如，`python process.py My_philosophy_for_a_happy_life.srt result.txt`。