import os
import sys

root_path = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.insert(0, root_path)
