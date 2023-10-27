from datetime import datetime
import json  

log_entries = []  

def log(log_type, log_file=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                log_result = {'result': result, 'log_type': log_type}
            except Exception as e:
                result = str(e)
                log_result = {'error': result, 'log_type': log_type}

            end_time = datetime.now()
            call_info = {
                'timestamp': start_time,
                'function_name': func.__name__,
                'args': args,
                'kwargs': kwargs,
            }
            call_info.update(log_result)
            log_entries.append(call_info)

            if log_file:
                with open(log_file, 'a') as file:
                    file.write(json.dumps(call_info) + "\n")  

            return result

        return wrapper

    return decorator

def get_logs():
    for entry in log_entries:
        yield entry

# Приклад використання
@log(log_type="info", log_file="log.txt")
def multiply(a, b):
    return a * b

@log(log_type="error", log_file="log.txt")
def divide(a, b):
    return a / b

result1 = multiply(3, 4)
result2 = divide(5, 0)

log_entries_generator = get_logs()

for entry in log_entries_generator:
    print(entry)
