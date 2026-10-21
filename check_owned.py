#!/usr/bin/env python3
"""Check deck JSON files against swudb_collection.csv.

Usage: python3 check_owned.py decks/<deck>/<file>.json [...]
Counts are summed across every printing of a card (Set, Name, Subtitle),
and only Premier-legal sets are read from the collection.
"""
import collections
import csv
import json
import re
import sys

LEGAL = ['ASH', 'HMW', 'JTL', 'LAW', 'LOF', 'SEC']

num2key = {}
for s in LEGAL:
    for c in json.load(open(f'cards/{s}_Cards.json'))['data']:
        num2key[(s, c['Number'])] = (c['Name'], c.get('Subtitle', ''))

owned = collections.Counter()
for r in csv.DictReader(open('swudb_collection.csv')):
    if r['Set'] not in LEGAL:
        continue
    num = re.sub(r'[a-z]+$', '', r['CardNumber'])  # e.g. SEC 571m -> 571
    key = num2key.get((r['Set'], num))
    if key is None:
        print(f"warning: no card for {r['Set']} {r['CardNumber']}", file=sys.stderr)
        continue
    owned[key] += int(r['Count'])

for f in sys.argv[1:]:
    d = json.load(open(f))
    print(f'== {f}')
    short = 0
    for e in [d['leader'], d['base']] + d['deck'] + d.get('sideboard', []):
        s, n = e['id'].split('_')
        key = num2key[(s, n)]
        need = e.get('count', 1)
        flag = ''
        if owned[key] < need:
            flag = f'  <-- short {need - owned[key]}'
            short += 1
        print(f"{e['id']:8} {key[0][:28]:28} need {need} own {owned[key]}{flag}")
    print('all owned' if short == 0 else f'{short} card(s) short')
