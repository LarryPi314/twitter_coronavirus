#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('hashtags', nargs='+')
parser.add_argument('--input_folder', default='outputs')
parser.add_argument('--output_path', default='plots/hashtag_timeline.png')
args = parser.parse_args()

import os
import glob
import json
import re
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'UnGraphic'
plt.rcParams['axes.unicode_minus'] = False

series = {hashtag: {} for hashtag in args.hashtags}

paths = sorted(glob.glob(os.path.join(args.input_folder, '*.lang')))

for path in paths:
    basename = os.path.basename(path)

    match = re.search(r'geoTwitter20-(\d\d)-(\d\d)\.zip\.lang$', basename)
    if not match:
        continue

    month = int(match.group(1))
    day = int(match.group(2))

    date = datetime.date(2020, month, day)
    day_of_year = date.timetuple().tm_yday

    with open(path) as f:
        counts = json.load(f)

    for hashtag in args.hashtags:
        daily_count = sum(counts.get(hashtag, {}).values())
        series[hashtag][day_of_year] = daily_count

plt.figure(figsize=(12, 6))

for hashtag in args.hashtags:
    xs = sorted(series[hashtag])
    ys = [series[hashtag][x] for x in xs]
    plt.plot(xs, ys, label=hashtag)

plt.xlabel('Day of Year')
plt.ylabel('Number of Tweets')
plt.title('Usage of Hashtag Coronavirus Plotted Across 2020 Days')
plt.legend()
plt.tight_layout()
plt.savefig(args.output_path)
plt.close()
