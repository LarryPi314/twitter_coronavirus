#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--output_folder',default='outputs')
args = parser.parse_args()

# imports
import os
import zipfile
import datetime 
import json
from collections import Counter,defaultdict

# load keywords
hashtags = [
    '#코로나바이러스',  # korean
    '#コロナウイルス',  # japanese
    '#冠状病毒',        # chinese
    '#covid2019',
    '#covid-2019',
    '#covid19',
    '#covid-19',
    '#coronavirus',
    '#corona',
    '#virus',
    '#flu',
    '#sick',
    '#cough',
    '#sneeze',
    '#hospital',
    '#nurse',
    '#doctor',
    ]

# initialize counters

counter_lang = defaultdict(lambda: Counter())
counter_country = defaultdict(lambda: Counter())

with zipfile.ZipFile(args.input_path) as archive:
    for filename in archive.namelist():
        print(datetime.datetime.now(), args.input_path, filename, flush=True)

        with archive.open(filename) as f:
            for line in f:
                try:
                    tweet = json.loads(line)
                except json.JSONDecodeError:
                    continue

                text = tweet.get('text', '').lower()
                lang = tweet.get('lang', 'und')

                place = tweet.get('place')
                country = None
                if isinstance(place, dict):
                    country = place.get('country_code')

                for hashtag in hashtags:
                    if hashtag in text:
                        counter_lang[hashtag][lang] += 1
                        counter_lang['_all'][lang] += 1

                        if country is not None:
                            counter_country[hashtag][country] += 1
                            counter_country['_all'][country] += 1

os.makedirs(args.output_folder, exist_ok=True)

output_path_base = os.path.join(
    args.output_folder,
    os.path.basename(args.input_path)
)

output_path_lang = output_path_base + '.lang'
output_path_country = output_path_base + '.country'

print('saving', output_path_lang)
with open(output_path_lang, 'w') as f:
    json.dump(counter_lang, f)

print('saving', output_path_country)
with open(output_path_country, 'w') as f:
    json.dump(counter_country, f)