from collections import OrderedDict
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_dict = OrderedDict()
        digit_log =[]
        for log in logs:
            identifier, content = log.split(" ",1)
            if content[0].isdigit():
                digit_log.append(log)
            else:
                letter_dict[log] = (content, identifier)
        def custom_sort(log):
            return letter_dict[log][0],letter_dict[log][1]
        sorted_letter_logs = sorted(letter_dict.keys(), key = custom_sort)
        print(sorted_letter_logs)

        return sorted_letter_logs + digit_log
