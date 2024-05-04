
int dhtpin = 3;

#include "DHT.h"

float temp;
float humid;

int MQ2_analog = A0;
int lpg, co, smoke;


DHT dht(dhtpin,DHT11);

void setup() {

  dht.begin();
  Serial.begin(9600); 
  
}

void loop() {

  temp = dht.readTemperature();
  humid = dht.readHumidity();

  Serial.println(temp); 
  Serial.println(humid);

  float* values= mq2.read(true);
  //lpg = values[0];
  lpg = mq2.readLPG();
  //co = values[1];
  co = mq2.readCO();
  //smoke = values[2];
  smoke = mq2.readSmoke();

  Serial.println(lpg);
  Serial.println(co);
  Serial.println(smoke);

}

