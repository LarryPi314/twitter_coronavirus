#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--output_path', required=True)
parser.add_argument('--percent', action='store_true')
args = parser.parse_args()

import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'UnGraphic'
plt.rcParams['axes.unicode_minus'] = False

with open(args.input_path) as f:
    counts = json.load(f)

data = dict(counts.get(args.key, {}))

if args.percent:
    totals = counts.get('_all', {})
    for k in list(data):
        total = totals.get(k, 0)
        data[k] = data[k] / total if total else 0

items = sorted(
    data.items(),
    key=lambda item: (item[1], item[0]),
    reverse=True
)[:10]

items = sorted(items, key=lambda item: (item[1], item[0]))

keys = [item[0] for item in items]
values = [item[1] for item in items]

plt.figure(figsize=(10, 6))
plt.bar(keys, values)
plt.xlabel('Language' if 'lang' in args.input_path else 'Country')
plt.ylabel('Number of Tweets')
plt.title(f'Top 10 results for {args.key}')
plt.tight_layout()
plt.savefig(args.output_path, dpi=200)
plt.close()