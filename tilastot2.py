import argparse
import statistics
parser = argparse.ArgumentParser()
parser.add_argument('num', type=int, nargs='*')
args = parser.parse_args()
print(f"Sum is {sum(args.num)}")
print(f"Max is {max(args.num)}")
print(f"Min is {min(args.num)}")
print(f"Mean is {statistics.mean(args.num)}")
print(f"Median is {statistics.median(args.num)}")
print(f"Mode is {statistics.mode(args.num)}")