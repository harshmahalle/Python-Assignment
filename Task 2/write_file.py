def write_list_to_file(file_path, string_list):
    with open(file_path, 'w') as file:
        for string in string_list:
            file.write(string + '\n')

# Example usage:
tasks = [
    "Complete the project report",
    "Attend team meeting",
    "Review code changes",
    "Update documentation",
    "Submit timesheet"
]

write_list_to_file('tasks_report.txt', tasks)
