# Grabs weather from unoffical Google Weather API, parses, and prints to console.

require 'open-uri'
require 'xmlsimple'

i = 0
place = ""
while (ARGV[i] != nil)
	if i == 0
		place = ARGV[0]
	else	
		place += " " + ARGV[i]
	end	
	i+=1
end

def getWeather(place)

	formattedPlace =  place.split(" ").join("+")
	contents = open('http://www.google.com/ig/api?weather='+formattedPlace) {|io| io.read}	
	weather = XmlSimple.xml_in(contents, { 'KeyAttr' => 'name' })

	current = weather['weather'][0]['current_conditions'][0]
	currentCondition = current['condition'][0]['data']
	currentTemp = current['temp_f'][0]['data']
	currentHumidity = current['humidity'][0]['data']
	forecast = weather['weather'][0]['forecast_conditions'][0]
	forecastHigh = forecast['high'][0]['data']
	forecastLow = forecast['low'][0]['data']
	forecastCondition = forecast['condition'][0]['data']

	header = "Weather for " + place
	headerSub = "========================"
	puts
	puts header
	puts "--------Current--------"
	puts "Condition:\t" + currentCondition
	puts "Temp:\t\t" + currentTemp + " F"
	puts "Humidity:\t" + currentHumidity	
	puts "-------Forecast--------"
	puts "High:\t\t" + forecastHigh + " F"
	puts "Low:\t\t" + forecastLow + " F"
	puts "Condition:\t" + forecastCondition
	puts "-----------------------"
	puts
	
end	

getWeather(place)	
