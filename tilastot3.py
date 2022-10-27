import argparse
parser = argparse.ArgumentParser()
parser.add_argument('num', type=int, nargs='*')
args = parser.parse_args()
print(sum(args.num))
print(max(args.num))
print(min(args.num))