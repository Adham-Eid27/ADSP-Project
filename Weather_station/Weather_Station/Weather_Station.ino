
int dhtpin = 3;

float rpm = 0;
unsigned long millisBefore;
volatile int holes;


#include "DHT.h"
#include <MQ2.h>

float temp;
float humid;

int MQ2_analog = A0;
int MQ135_analog = A1;
int lpg, co, smoke, air_quality;

MQ2 mq2(MQ2_analog);


DHT dht(dhtpin,DHT11);

void setup() {

  pinMode(2, INPUT);
  attachInterrupt(digitalPinToInterrupt(2), count, FALLING);

  dht.begin();
  Serial.begin(9600); 
  
  mq2.begin();
}

void loop() {

  if (millis() - millisBefore > 1000) {
    rpm = (holes / 12.0)*60;
    holes = 0;
    millisBefore = millis();
  }

  temp = dht.readTemperature();
  humid = dht.readHumidity();

  Serial.println(temp); 
  Serial.println(humid);

  lpg = mq2.readLPG();
  co = mq2.readCO();
  smoke = mq2.readSmoke();

  air_quality = analogRead(MQ135_analog);

  Serial.println(lpg);
  Serial.println(co);
  Serial.println(smoke);

  Serial.println(air_quality);

  Serial.println(rpm);


}

void count() {
  holes++;
}


