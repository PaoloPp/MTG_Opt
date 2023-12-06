import subprocess

import constants as ct
from decks import genome_to_decklist, write_decklist

def build_cmd(candidate_name, opponent_name, nr_matches):
    return ['java', '-Xmx1024m', '-jar',
            'forge-gui-desktop-1.5.61-SNAPSHOT-jar-with-dependencies.jar', 'sim',
            '-d', candidate_name, opponent_name,
            '-n', nr_matches, '-f', 'sealed']



total_damage = 0
wins = 0
# colors,lands = colorsymbols_in_deck(CARDS, decklist)

for challenger in ct.OPPONENTS:
    total_wins=0
    for i in range(20):
        for opponent in ct.OPPONENTS:
            cmd = build_cmd(challenger, opponent, ct.MATCHES_PER_OPPONENT)
            p = subprocess.Popen(cmd, cwd=ct.FORGE_PATH, stdout=subprocess.PIPE)
            for line in p.stdout:
                line = line.decode("utf-8").strip()
                #print(line)
                # if 'combat damage to Ai(2' in line:
                #     hit_event = line.split(' ')
                #     # print(hit_event) #For debugging
                #     damage_index = hit_event.index('deals') + 1
                #     damage = int(hit_event[damage_index])
                #     total_damage += damage
                if 'Match result' in line:
                    result = line.split(' ')
            wins += int(result[3])
            p.wait()
            total_wins+=wins