# 1.3.: Keeping the Last N Items

# Problem: We want to keep a limited history of the last few items seen during iteration or during some other kind of processing.

# Solutions: Keeping the limited history is a perfect use for a collections.deque. 

from collections import deque

def search(lines, patterns, history=5):
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)

