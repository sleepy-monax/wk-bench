#!/usr/bin/env python3

import argparse
import psutil
import sys
import time

def tree_memory(psutil_process):
    """
    Calculate the memory usage of a process and its children.

    :param psutil_process: The process to calculate the memory usage of
    :return: The memory usage of the process and its children in bytes
    """
    memory = psutil_process.memory_info().rss
    for child in psutil_process.children():
        memory += tree_memory(child)
    return memory

def monitor(pid, interval, output):
    """
    Monitor a process and its children CPU and memory usage.

    :param pid: The pid of the process to monitor
    :param interval: The interval in seconds between each measurement
    :param output: The file to write the measurements to
    """
    start = time.time()
    process = psutil.Process(pid)
    max_memory = 0
    with open(output, 'w') as f:
        f.write('time,cpu,memory\n')
        while process.is_running() and process.status() != psutil.STATUS_ZOMBIE:
            cpu = process.cpu_percent(interval=interval)
            memory = tree_memory(process)
            max_memory = max(max_memory, memory)
            f.write('{},{},{}\n'.format(time.time() - start, cpu, memory))
        f.write('{},0,{}\n'.format(time.time() - start, max_memory))
        f.flush()
        print('Process {} is not running anymore (max memory: {}Mib)'.format(pid, max_memory / 1024 / 1024))

def monitorSubprocess(args, interval, output):
    """
    Monitor a subprocess CPU and memory usage.

    :param args: The arguments to pass to the subprocess
    :param interval: The interval in seconds between each measurement
    :param output: The file to write the measurements to
    """
    process = psutil.Popen(args)
    monitor(process.pid, interval, output)
    process.wait() # *charge shotgun* DIE DIE DIE ZOMBIE!!!

def main():
    parser = argparse.ArgumentParser(description='Monitor a process and its children CPU and memory usage.')
    parser.add_argument('interval', type=float, help='The interval in seconds between each measurement')
    parser.add_argument('output', type=str, help='The file to write the measurements to')
    parser.add_argument('command', nargs=argparse.REMAINDER, help='The command to run')
    args = parser.parse_args()

    if len(args.command) == 0:
        parser.print_help()
        sys.exit(1)
    
    monitorSubprocess(args.command, args.interval, args.output)

if __name__ == '__main__':
    main()
