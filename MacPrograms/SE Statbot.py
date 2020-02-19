#INDEX:
#   1: general module setup
#   2: discord module setup
#   3: google module setup
#   4: message responses
#       4.1: verification as valid message
#       4.2: row finder
#       4.3: full_summary
#           4.3.1: placeholder message
#           4.3.2: game statistics
#           4.3.3: game percentages
#           4.3.4: alignment statistics
#           4.3.5: actual message
#       4.4: quick_summary
#           4.4.1: placeholder message
#           4.4.2: statistics
#           4.4.3: actual message
#   5: run token


#--------------------------------------------------
#INDEX 1


import re #documentation: https://docs.python.org/3/library/re.html


#--------------------------------------------------
#INDEX 2


import discord #documentation: http://discordpy.readthedocs.io/en/latest/api.html

TOKEN = 'NDU0NjQ4Mzc1ODcxMTQzOTM2.DfwgAg.vpZccChlM7B2okJgc4GFqzPTF6E'
client = discord.Client()


#--------------------------------------------------
#INDEX 3


import gspread #documentation: https://gspread.readthedocs.io/en/latest/
from oauth2client.service_account import ServiceAccountCredentials #documentation: http://oauth2client.readthedocs.io/en/latest/source/oauth2client.service_account.html

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive'] #['https://www.googleapis.com/auth/devstorage.read_only'] <-- alternate scope
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/evanconway/Downloads/SE Statbot-d2b7e39289e4.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_url('https://docs.google.com/spreadsheets/d/1CxrgdT4Xd8J0N3CuVmkVRryMeIdm93H8rzv8-YlP0kw/edit#gid=1302539305').sheet1


#--------------------------------------------------
#INDEX 4


@client.event
async def on_message(message):


    #--------------------------------------------------
    #INDEX 4.1


    if message.author == client.user:
        return

    validCommand = re.compile('^:(\w)*|$')
    if validCommand.search(str(message.content))[0] == '':
        return


    #--------------------------------------------------
    #INDEX 4.2

    messageStart = message.content
    messageStart = str(messageStart.split(' ', 1)[0])
    if messageStart in [':top']:
        True == True
        
    else:
        messageAlt = str(message.content)
        messageAlt = messageAlt.split(' ', 1)
        try:
            coordinates = str(wks.find(messageAlt[1]))
        except:
            await client.send_message(message.channel, str(message.author.mention) + ' that is not a valid input.')
        coordinates = coordinates.split('R', 1)
        row = coordinates[1]
        row = row.split('C', 1)
        row = str(row[0])


    #--------------------------------------------------
    #INDEX 4.3

    
    if message.content.startswith(':full_summary'):

        
        #--------------------------------------------------
        #INDEX 4.3.1

        
        player = str(wks.acell('A' + row).value)
        em = discord.Embed(title = 'Full Summary of ' + player, description = 'Locating data...')
        msg = await client.send_message(message.channel, embed = em)
        
        
        #--------------------------------------------------
        #INDEX 4.3.2

        
        first = str(wks.acell('D' + row).value)
        total = str(wks.acell('E' + row).value)
        played = str(wks.acell('F' + row).value)
        minusBI = str(wks.acell('G' + row).value)
        GM = str(wks.acell('BG' + row).value)
        mod = str(wks.acell('BH' + row).value)
        inactive = str(wks.acell('O' + row).value)
        active = str(int(played) - int(inactive))
        broken = str(int(played) - int(minusBI) - int(inactive))
        

        #--------------------------------------------------
        #INDEX 4.3.3


        playedP = str(round((int(played) / int(total))*100, 1))
        GMP = str(round((int(GM) / int(total))*100, 1))
        brokenP = str(round((int(broken) / int(total))*100, 1))
        activeP = str(round((int(active) / int(total))*100, 1))
        inactiveP = str(round((int(inactive) / int(total))*100, 1))


        #--------------------------------------------------
        #INDEX 4.3.4

        
        good = str(wks.acell('H' + row).value)
        evil = str(wks.acell('I' + row).value)
        other = str(int(wks.acell('J' + row).value) + int(wks.acell('K' + row).value) + int(wks.acell('L' + row).value))
        goodWBI = str(wks.acell('P' + row).value)
        evilWBI = str(wks.acell('Q' + row).value)
        otherWBI = str(int(wks.acell('S' + row).value) + int(wks.acell('T' + row).value) + int(wks.acell('U' + row).value))

        
        #--------------------------------------------------
        #INDEX 4.3.5


        goodP = str(round((int(good) / int(minusBI))*100, 1))
        evilP = str(round((int(evil) / int(minusBI))*100, 1))
        otherP = str(round((int(other) / int(minusBI))*100, 1))
        goodPWBI = str(round((int(goodWBI) / int(played))*100, 1))
        evilPWBI = str(round((int(evilWBI) / int(played))*100, 1))
        otherPWBI = str(round((int(otherWBI) / int(played))*100, 1))


        #--------------------------------------------------
        #INDEX 4.3.6

        
        em = discord.Embed(title = 'Full Summary of ' + player,
        description = '**Game Statistics:**' + '\n'
        'First Game: ' + first + '\n'
        'Games as GM: ' + GM + '\n'
        'Games as Moderator: ' + mod + '\n'
        'Games as Active Player: ' + active + '\n'
        'Games as Inactive Player: ' + inactive + '\n' + '\n'
        '**Game Percentages:**' + '\n'
        'Percent of Games as GM: ' + GMP + '%' + '\n'
        'Percent of Games as Active Player: ' + activeP + '%' + '\n'
        'Percent of Games as Inactive: ' + inactiveP + '%' + '\n' + '\n'
        '**Alignment Statistics:**' + '\n'
        'Games as Villager (Accurate): ' + good + '\n'
        'Games as Eliminator (Accurate): ' + evil + '\n'
        'Games as Other Alignment (Accurate): ' + other + '\n' + '\n'
        'Games as Villager (With Broken/Inactive): ' + goodWBI + '\n'
        'Games as Eliminator (With Broken/Inactive): ' + evilWBI + '\n'
        'Games as Other Alignment (With Broken/Inactive): ' + otherWBI + '\n' + '\n'
        '**Alignment Percentages:**' + '\n'
        'Percent of Games as Villager (Accurate): ' + goodP + '%' + '\n'
        'Percent of Games as Eliminator (Accurate): ' + evilP + '%' + '\n'
        'Percent of Games as Other Alignment (Accurate): ' + otherP + '%' + '\n' + '\n'
        'Percent of Games as Villager (With Broken/Inactive): ' + goodPWBI + '%' + '\n'
        'Percent of Games as Eliminator (With Broken/Inactive): ' + evilPWBI + '%' + '\n'
        'Percent of Games as Other Alignment (With Broken/Inactive): ' + otherPWBI + '%' + '\n' +'\n')
        
        await client.edit_message(msg, embed = em)


    #--------------------------------------------------
    #INDEX 4.4


    elif message.content.startswith(':quick_summary'):


        #--------------------------------------------------
        #INDEX 4.4.1


        player = str(wks.acell('A' + row).value)
        em = discord.Embed(title = 'Quick Summary of ' + player, description = 'Locating data...')
        msg = await client.send_message(message.channel, embed = em)


        #--------------------------------------------------
        #INDEX 4.4.2


        first = str(wks.acell('D' + row).value)
        played = str(wks.acell('F' + row).value)
        GM = str(wks.acell('BG' + row).value)
        inactive = str(wks.acell('O' + row).value)
        active = str(int(played) - int(inactive))
        
        good = str(wks.acell('H' + row).value)
        evil = str(wks.acell('I' + row).value)
        other = str(int(wks.acell('J' + row).value) + int(wks.acell('K' + row).value) + int(wks.acell('L' + row).value))

        winP = str(wks.acell('W' + row).value)
        survivalP = str(wks.acell('AQ' + row).value)


        #--------------------------------------------------
        #INDEX 4.4.3


        em = discord.Embed(title = 'Quick Summary of ' + player,
        description = 'First Game: '+ first + '\n'
        'Games as GM: ' + GM + '\n'
        'Games as Active Player: ' + active + '\n'
        'Games as Inactive Player: ' + inactive + '\n' + '\n'
        'Games as Villager: ' + good + '\n'
        'Games as Eliminator: ' + evil + '\n'
        'Games as Other Alignment: ' + other + '\n' + '\n'
        'Win Percentage: ' + winP + '%' + '\n'
        'Survival Percentage: ' + survivalP + '%' + '\n')
        
        await client.edit_message(msg, embed = em)

    #--------------------------------------------------
    #INDEX 4.4


    if message.content.startswith(':top'):
        
        
        #--------------------------------------------------
        #INDEX 4.4.1
        
        
        leaderboardLength = message.content
        leaderboardString = ''
        try:
            leaderboardLength = leaderboardLength.split(' ', 1)
        except:
            await client.send_message(message.channel, str(message.author.mention) + ' that is not a valid input.')
        
        
        #--------------------------------------------------
        #INDEX 4.4.2

        leaderboardList = wks.range('A4:A' + str(int(leaderboardLength[1]) + 3))
        
        for number in range(int(leaderboardLength[1])):
            leaderboardString += str(number + 1) + '. ' + str(leaderboardList[number].value) + '\n'

        try:
            em = discord.Embed(title = 'Top ' + str(leaderboardLength[1]) + ' Players', description = leaderboardString)
            await client.send_message(message.channel, embed = em)
        except:
            await client.send_message(message.channel, str(message.author.mention) + ' that is not a valid input.')


#--------------------------------------------------
#INDEX 5


client.run(TOKEN)
