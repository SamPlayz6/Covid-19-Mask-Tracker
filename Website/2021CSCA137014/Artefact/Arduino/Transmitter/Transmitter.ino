#include <RH_ASK.h>
#include <SPI.h>

#include <CCS811.h>
CCS811 sensor;

#include <dht.h>
dht DHT;
#define DHT11_PIN 7

RH_ASK rf_driver;

String humidity;
String temperature;
String VOC;
String CO2;
String str_out;

void setup() {
  //LED Setup
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  
  //Initiate RF Communication
  Serial.begin(9600);
  rf_driver.init();

  //Indicates if connection fails
  while(sensor.begin() != 0){
      Serial.println("failed to init chip, please check if the chip connection is fine");
      delay(1000);
  }
   sensor.setMeasCycle(sensor.eCycle_250ms);
}

void loop() {
  // CO2 Sensor
    delay(1000);
    if(sensor.checkDataReady() == true){
        Serial.print("CO2: ");
        Serial.print(sensor.getCO2PPM());
        Serial.print("ppm, TVOC: ");
        Serial.print(sensor.getTVOCPPB());
        Serial.println("ppb");
        
    } else {
        Serial.println("Data is not ready!");
    }
    sensor.writeBaseLine(0x847B);


  // Humidity Sensor
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity = ");
  Serial.println(DHT.humidity);
  Serial.println();


  // Transmittion
  humidity = String(float(DHT.humidity));
  temperature = String(float(DHT.temperature));
  CO2 = String(sensor.getCO2PPM());
  VOC = String(sensor.getTVOCPPB());
  
  str_out = humidity + ", " + temperature + ", " + CO2 + ", " + VOC + ",";

  const char *msg = str_out.c_str();
  //const char *msg = "Welcome World";

  rf_driver.send((uint8_t *)msg,strlen(msg));
  rf_driver.waitPacketSent();


  //LED
  if (sensor.getCO2PPM() > 2000){
    digitalWrite(9, HIGH);
  }
  else{
  digitalWrite(9,LOW);
  }

  if (sensor.getCO2PPM() > 2000){
    digitalWrite(8,LOW);
  }
  else{
    digitalWrite(8,HIGH);
    }

  
  delay(1000);
  
}
