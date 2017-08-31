import random

import TOKEN
import discord


bot = discord.Client()
bot.run(TOKEN.TOKEN)


def newgame():
    bot.memory['secret_hitler'] = {'players': [],
                               'player_list_copy': [],
                               'setup_phase': False,
                               'board_state': 0,  # three board states depending on number of players
                               'liberal_policies': 0,  # Liberals win with 5 Liberal Policies enacted
                               'failed_votes': 0,  # Maximum of 3 failed Elections, else Chaos
                               'fascist_policies': 0,  # Fascists win with 3 Policies and Hitler as Chancellor
                               'president': None,
                               'chancellor_candidate': None,
                               'prev_president': None,
                               'former_president': None,  # necessary for the special election process
                               'election_phase': False,
                               'chancellor': None,
                               'players_who_voted': {},
                               'former_chancellor': None,
                               'yes_votes': 0,
                               'no_votes': 0,
                               'deck': ['Liberal', 'Liberal', 'Liberal', 'Liberal', 'Liberal', 'Liberal', 'Fascist',
                                        'Fascist', 'Fascist', 'Fascist', 'Fascist', 'Fascist', 'Fascist', 'Fascist',
                                        'Fascist', 'Fascist', 'Fascist'],
                               'drawn_cards': [],
                               'discard_pile': [],
                               'liberals': [],
                               'fascists': [],
                               'kill_phase': False,
                               'vote_phase': False,
                               'reveal_phase': False,
                               'special_election_phase': False,
                               'chaos_phase': False,
                               'veto_switch': False,
                               'policy_phase': False,
                               'dead_players': [],
                               'num_of_fascists': 0,
                               # 2 for 5-6 players, 3 for 7-8 players, 4 for 9-10 players, includes Hitler
                               'num_of_liberals': 0,
                               # 3-4 for 5-6 players, 4-5 for 7-8 players, 5-6 for 9-10 players
                               'Hitler': None,  # randomly chosen among the fascist players
                               'game_ongoing': False,
                               'move_on': False,
                               'owner': 'VereorNox'}




def join_game(message):
    if bot.memory['secret_hitler']['setup_phase'] == True:
        # here, we check for the user's ID, rather than their nick, because people can change their nicknames and usernames at any time on Discord; the ID is the only constant
        if message.author.id not in bot.memory['secret_hitler']['players'] and len(
                bot.memory['secret_hitler']['players']) < 10:
            bot.memory['secret_hitler']['players'].append(message.author.id)
            bot.send_message(message.channel, message.author.display_name + ' has joined up!')
    else:
        bot.send_message(message.channel, 'No game has been started yet, or a game is currently ongoing.')


def prepare_to_start(message):
    print(bot.memory.keys())
    if 'secret_hitler' not in bot.memory or bot.memory['secret_hitler']['game_ongoing'] == False and bot.memory['secret_hitler']['setup_phase'] == False:
        newgame(bot)
        random.shuffle(bot.memory['secret_hitler']['deck'])
        bot.memory['secret_hitler']['setup_phase'] = True
        bot.send_message(message.channel, "Someone has started a game of Secret Hitler! Type .join to join! When 5 players have assembled, type .start to start!", '#games')
        bot.memory['secret_hitler']['players'].append(message.author.id)
        bot.send_message(message.author.display_name + " has joined up! Type .flee to leave with your tail tucked between your legs!", '#games')
    else:
        bot.send_message(message.channel, "A game is already going on. Please wait until it is finished to start another game.", '#games')



prefix = '.'


@bot.event
async def on_message(message):
    if message.content.startswith(prefix):
        # no need to check for commands if it doesn't start with prefix
        if message.channel.is_private:
            return
        else:
            if message.content.startswith(prefix+'join'):
                join_game(message)
            if message.content.startswith(prefix+'hitler'):
                prepare_to_start()

    else:
        bot.send_message(message.channel, 'fuck you')

