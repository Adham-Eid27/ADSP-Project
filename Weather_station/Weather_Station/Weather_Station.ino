
int dhtpin = 3;

#include "DHT.h"
#include <MQ2.h>

float temp;
float humid;

int MQ2_analog = A0;
int lpg, co, smoke;

MQ2 mq2(MQ2_analog);


DHT dht(dhtpin,DHT11);

void setup() {

  dht.begin();
  Serial.begin(9600); 
  
  mq2.begin();
}

void loop() {

  temp = dht.readTemperature();
  humid = dht.readHumidity();

  Serial.println(temp); 
  Serial.println(humid);

  lpg = mq2.readLPG();
  co = mq2.readCO();
  smoke = mq2.readSmoke();

  Serial.println(lpg);
  Serial.println(co);
  Serial.println(smoke);

}

