
int dhtpin = 3;

#include "DHT.h"

float temp;
float humid;


DHT dht(dhtpin,DHT11);

void setup() {

  dht.begin();
  Serial.begin(9600); 
  
}

void loop() {

  temp = dht.readTemperature();
  humid = dht.readHumidity();

  Serial.println(temp); //serial print 1 Temp
  Serial.println(humid); //serial print 2 Humid
}

