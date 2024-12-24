import subprocess

# 定义要执行的命令
command = ['python', 'evaluate.py', 'realcap/01.gif']

try:
    # 执行命令
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    
    # 输出命令的标准输出和标准错误
    print("Standard Output:", result.stdout)
    print("Standard Error:", result.stderr)
    
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
