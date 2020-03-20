import datetime
import re

# print(re.search(r'\d{4}-\d{2}-\d{2}', 'xxxx1990-12-20xxxx').group(0))
# print(re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', 'xxxx2005-06-04T18:37:11xxxx').group(0))
# print(re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}', 'xxxx2005-06-04T18:37:11.111xxxx').group(0))
#
# pattern = re.compile(r'(\d{4}-\d{2}-\d{2})((T\d{2}:\d{2}:\d{2}|))((.\d{3})|)')
# print(pattern.search('xxxx2005-06-04T18:37:11.111xxxx').group(0))


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M')
        return date_text + ':00'
    except ValueError:
        pass

    return date_text

result =validate('2020-03-16 01:17')

print("result:{}".format(result))

