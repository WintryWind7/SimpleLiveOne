import subprocess

# 设置 RTMP 流的 URL
rtmp_url = "rtmp://wintrywind.top:1935/live/test"

# 使用 subprocess 调用 ffplay 播放 RTMP 流
subprocess.run(['ffplay', rtmp_url])
