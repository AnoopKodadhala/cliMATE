
import discord
from discord.ext import commands
from io import BytesIO
import requests
from bs4 import BeautifulSoup

#Used env variables to protect token
import os
key = os.environ.get('cliMATE_KEY')

intents = discord.Intents.all()
client = commands.Bot(command_prefix='?', intents=intents)


@client.event
async def on_ready():
    print('cliMATE is now online'.format(client))

@client.command()
async def source(ctx):
    await ctx.send('https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt')
    await ctx.send('https://climate.nasa.gov/')
    

@client.command()
async def co2(ctx):
    URL = 'https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt'
    page = requests.get(URL)
    co2Num = page.text[-42:-36]
    year = page.text[-69:-63]
    month = page.text[-61]

    await ctx.send('The concentration of carbon dioxide as of ( '+str(month)+'/'+str(year)+') is: '+str(co2Num)+ " part's per million")

@client.command()
async def sealevel(ctx):
    URL = "https://climate.nasa.gov/vital-signs/sea-level/"
    r = requests.get(URL)
    a = BeautifulSoup(r.content, 'html.parser')
    date = a.find('span', class_='month_year')
    date = date.text
    date = date[1:-1]

    b = a.find('div', class_='value')
    b = b.text.split()
    amount = b[0]

    await ctx.send('As of '+ str(date)+' the sea level has risen '+str(amount)+' milimeters since 1993')

@client.command()
async def ice(ctx):


    await ctx.send('Antarctica is losing ice mass (melting) at an average rate of about 150 billion tons per year')
    await ctx.send(file=discord.File('LandIceAntarctica.png'))
@client.command()
async def NOAA(ctx, month='july', year='2022'):
    monthValues = {
        'january': '01'
        , 'february': '02'
        , 'march': '03'
        , 'april': '04'
        , 'may': '05'
        , 'june': '06'
        , 'july': '07'
        , 'august': '08'
        , 'september': '09'
        , 'october': '10'
        , 'novemeber': '11'
        , 'december': '12'
        , 'jan': '01'
        , 'feb': '02'
        , 'mar': '03'
        , 'apr': '04'
        , 'aug': '08'
        , 'sept': '09'
        , 'oct': '10'
        , 'nov': '11'
        , 'dec': '12'
    }
    if month.lower() in monthValues:
        month = monthValues[month.lower()]

        URL = "https://www.ncei.noaa.gov/news/global-climate-" + year + month
        r = requests.get(URL)
        a = BeautifulSoup(r.content, 'html.parser')
        b = a.find('div', class_='clearfix text-formatted')
        c = b.find('p').text
        print(c)

        await ctx.send(str(c))
    else:
        await ctx.send('error, either invalid date/year or no report at that time')

client.run(key)
