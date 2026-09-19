from collector.processes import get_processes

processes = get_processes()

#for process, cpu, memory in processes:
#    print(process, "CPU:", cpu, "Memory:", memory)

processes = sorted(processes, key=lambda x: x[1], reverse=True)

for process, cpu, memory in processes[:10]:
    print(process.name(), "CPU:", cpu, "Memory:", memory)