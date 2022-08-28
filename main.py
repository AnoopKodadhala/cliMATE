
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random

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
    await ctx.send('https://www.un.org/en/climatechange/science/causes-effects-climate-change')


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

@client.command()
async def cause(ctx):
    factList = [
        'Fossil fuels – coal, oil and gas – are by far the largest contributor to global climate change, accounting for over 75 per cent of global greenhouse gas emissions and nearly 90 per cent of all carbon dioxide emissions.',
        'Consuming too much - Your home and use of power, how you move around, what you eat and how much you throw away all contribute to greenhouse gas emissions. So does the consumption of goods such as clothing, electronics, and plastics. A large chunk of global greenhouse gas emissions are linked to private households. Our lifestyles have a profound impact on our planet. The wealthiest bear the greatest responsibility: the richest 1 per cent of the global population combined account for more greenhouse gas emissions than the poorest 50 per cent.',
        'Powering buildings - Globally, residential and commercial buildings consume over half of all electricity. As they continue to draw on coal, oil, and natural gas for heating and cooling, they emit significant quantities of greenhouse gas emissions. Growing energy demand for heating and cooling, with rising air-conditioner ownership, as well as increased electricity consumption for lighting, appliances, and connected devices, has contributed to a rise in energy-related carbon-dioxide emissions from buildings in recent years.',
        'Cutting down forests - Cutting down forests to create farms or pastures, or for other reasons, causes emissions, since trees, when they are cut, release the carbon they have been storing. Each year approximately 12 million hectares of forest are destroyed. Since forests absorb carbon dioxide, destroying them also limits nature’s ability to keep emissions out of the atmosphere. Deforestation, together with agriculture and other land use changes, is responsible for roughly a quarter of global greenhouse gas emissions.',
        'Using transportation - Most cars, trucks, ships, and planes run on fossil fuels. That makes transportation a major contributor of greenhouse gases, especially carbon-dioxide emissions. Road vehicles account for the largest part, due to the combustion of petroleum-based products, like gasoline, in internal combustion engines. But emissions from ships and planes continue to grow. Transport accounts for nearly one quarter of global energy-related carbon-dioxide emissions. And trends point to a significant increase in energy use for transport over the coming years. ',
        'Producing food - Producing food causes emissions of carbon dioxide, methane, and other greenhouse gases in various ways, including through deforestation and clearing of land for agriculture and grazing, digestion by cows and sheep, the production and use of fertilizers and manure for growing crops, and the use of energy to run farm equipment or fishing boats, usually with fossil fuels. All this makes food production a major contributor to climate change. And greenhouse gas emissions also come from packaging and distributing food.  ',

    ]

    await ctx.send(random.choice(factList))

@client.command()
async def effect(ctx):
    factList = [
        'Hotter temperatures - As greenhouse gas concentrations rise, so does the global surface temperature. The last decade, 2011-2020, is the warmest on record. Since the 1980s, each decade has been warmer than the previous one. Nearly all land areas are seeing more hot days and heat waves. Higher temperatures increase heat-related illnesses and make working outdoors more difficult. Wildfires start more easily and spread more rapidly when conditions are hotter. Temperatures in the Arctic have warmed at least twice as fast as the global average.',
        "More severe storms - Destructive storms have become more intense and more frequent in many regions. As temperatures rise, more moisture evaporates, which exacerbates extreme rainfall and flooding, causing more destructive storms. The frequency and extent of tropical storms is also affected by the warming ocean. Cyclones, hurricanes, and typhoons feed on warm waters at the ocean surface. Such storms often destroy homes and communities, causing deaths and huge economic losses.",
        'Increased drought - Climate change is changing water availability, making it scarcer in more regions. Global warming exacerbates water shortages in already water-stressed regions and is leading to an increased risk of agricultural droughts affecting crops, and ecological droughts increasing the vulnerability of ecosystems. Droughts can also stir destructive sand and dust storms that can move billions of tons of sand across continents. Deserts are expanding, reducing land for growing food. Many people now face the threat of not having enough water on a regular basis.',
        'A warming, rising ocean - The ocean soaks up most of the heat from global warming. The rate at which the ocean is warming strongly increased over the past two decades, across all depths of the ocean. As the ocean warms, its volume increases since water expands as it gets warmer. Melting ice sheets also cause sea levels to rise, threatening coastal and island communities. In addition, the ocean absorbs carbon dioxide, keeping it from the atmosphere. But more carbon dioxide makes the ocean more acidic, which endangers marine life and coral reefs.',
        'Loss of species - Climate change poses risks to the survival of species on land and in the ocean. These risks increase as temperatures climb. Exacerbated by climate change, the world is losing species at a rate 1,000 times greater than at any other time in recorded human history. One million species are at risk of becoming extinct within the next few decades. Forest fires, extreme weather, and invasive pests and diseases are among many threats related to climate change. Some species will be able to relocate and survive, but others will not.',
        'Not enough food - Changes in the climate and increases in extreme weather events are among the reasons behind a global rise in hunger and poor nutrition. Fisheries, crops, and livestock may be destroyed or become less productive. With the ocean becoming more acidic, marine resources that feed billions of people are at risk. Changes in snow and ice cover in many Arctic regions have disrupted food supplies from herding, hunting, and fishing. Heat stress can diminish water and grasslands for grazing, causing declining crop yields and affecting livestock.',
        'More health risks - Climate change is the single biggest health threat facing humanity. Climate impacts are already harming health, through air pollution, disease, extreme weather events, forced displacement, pressures on mental health, and increased hunger and poor nutrition in places where people cannot grow or find sufficient food. Every year, environmental factors take the lives of around 13 million people. Changing weather patterns are expanding diseases, and extreme weather events increase deaths and make it difficult for health care systems to keep up.',
        'Poverty and displacement - Climate change increases the factors that put and keep people in poverty. Floods may sweep away urban slums, destroying homes and livelihoods. Heat can make it difficult to work in outdoor jobs. Water scarcity may affect crops. Over the past decade (2010–2019), weather-related events displaced an estimated 23.1 million people on average each year, leaving many more vulnerable to poverty. Most refugees come from countries that are most vulnerable and least ready to adapt to the impacts of climate change.',
    ]

    await ctx.send(random.choice(factList))

@client.command()
async def change(ctx):
    factList = [
        'Save energy at home - Much of our electricity and heat are powered by coal, oil, and gas. Use less energy by lowering your heating and cooling, switching to LED light bulbs and energy-efficient electric appliances, washing your laundry with cold water, or hanging things to dry instead of using a dryer.',
        'Walk, bike, or take public transport - The world’s roadways are clogged with vehicles, most of them burning diesel or gasoline. Walking or riding a bike instead of driving will reduce greenhouse gas emissions — and help your health and fitness. For longer distances, consider taking a train or bus. And carpool whenever possible.',
        'Eat more vegetables - Eating more vegetables, fruits, whole grains, legumes, nuts, and seeds, and less meat and dairy, can significantly lower your environmental impact. Producing plant-based foods generally results in fewer greenhouse gas emissions and requires less energy, land, and water.',
        'Consider your travel - Airplanes burn large amounts of fossil fuels, producing significant greenhouse gas emissions. That makes taking fewer flights one of the fastest ways to reduce your environmental impact. When you can, meet virtually, take a train, or skip that long-distance trip altogether.',
        "Throw away less food - When you throw food away, you're also wasting the resources and energy that were used to grow, produce, package, and transport it. And when food rots in a landfill, it produces methane, a powerful greenhouse gas. So use what you buy and compost any leftovers.",
        'Reduce, reuse, repair & recycle - Electronics, clothes, and other items we buy cause carbon emissions at each point in production, from the extraction of raw materials to manufacturing and transporting goods to market. To protect our climate, buy fewer things, shop second-hand, repair what you can, and recycle.',
        "Change your home's source of energy - Ask your utility company if your home energy comes from oil, coal, or gas. If possible, see if you can switch to renewable sources such as wind or solar. Or install solar panels on your roof to generate energy for your home.",
        'Switch to an electric vehicle - If you plan to buy a car, consider going electric, with more and cheaper models coming on the market. Even if they still run on electricity produced from fossil fuels, electric cars help reduce air pollution and cause significantly fewer greenhouse gas emissions than gas or diesel-powered vehicles.',
    ]


    await ctx.send(random.choice(factList))
client.run(key)
