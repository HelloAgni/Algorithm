from datetime import datetime, timedelta

DAY_START = datetime.strptime('09:00', '%H:%M')
DAY_END = {'start': '21:00', 'stop': '21:00'}
VISIT_DURATION = timedelta(minutes=30)

busy = [
    {'start': '10:30',
     'stop': '10:50'
     },
    {'start': '18:40',
     'stop': '18:50'
     },
    {'start': '14:40',
     'stop': '15:50'
     },
    {'start': '16:40',
     'stop': '17:20'
     },
    {'start': '20:05',
     'stop': '20:20'
     }
]


def find_free(args: list[dict]) -> tuple[list[dict], list]:
    """
    Returns the lists of dicts with formated datetime to str.

            Parameters:
                    args (list): A list of dicts

            Returns:
                    result (list): A list of dicts formated datetime to str
                    result_v2 (list): List of formated datetime to str
    """
    new_busy = sorted(args, key=lambda s: s['start'])

    new_busy.append(DAY_END)

    result = []
    result_v2 = []

    current_start = DAY_START
    for _ in new_busy:
        while current_start < datetime.strptime(_['start'], '%H:%M'):
            check_dur = current_start + VISIT_DURATION
            if check_dur <= datetime.strptime(_['start'], '%H:%M'):
                result.append({'start_visit': '{:02d}:{:02d}'.format(
                               current_start.hour, current_start.minute),
                               'end_visit': '{:02d}:{:02d}'.format(
                               check_dur.hour, check_dur.minute)
                               })
                result_v2.append('{:02d}:{:02d}'.format(
                    current_start.hour, current_start.minute))
            current_start += VISIT_DURATION
        current_start = datetime.strptime(_['stop'], '%H:%M')

    return result, result_v2


print(*find_free(busy), sep='\n')
