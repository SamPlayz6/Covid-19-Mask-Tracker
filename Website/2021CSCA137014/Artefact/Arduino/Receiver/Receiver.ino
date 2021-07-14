#include <RH_ASK.h>
#include <SPI.h>
  RH_ASK rf_driver;
  
void setup() {
  //Initiate RF Communication 
  rf_driver.init();
  Serial.begin(9600);
}

void loop() {
  //Reading data
  uint8_t buf[24];
  uint8_t buflen = sizeof(buf);
  if (rf_driver.recv(buf,&buflen))

    Serial.println((char*)buf);
    delay(1000);
  }
