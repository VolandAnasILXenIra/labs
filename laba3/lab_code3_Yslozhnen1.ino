#include <Wire.h> 
#include <LiquidCrystal_I2C.h> 
#include "DHT.h" 
#include "MQ135.h" 
 
// Подключение LCD дисплея 
LiquidCrystal_I2C lcd(0x27, 16, 2); 
 
// Подключение датчика DHT11 
#define DHTPIN A0 
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE); 
 
// Подключение датчика MQ135 
#define ANALOGPIN A1 
MQ135 gasSensor = MQ135(ANALOGPIN); 
 
// Подключение датчика пламени 
int flameSensorPin = 4; 
 
// Подключение насоса 
#define PUMP_PIN 3 
 
void setup() { 
  lcd.init(); 
  lcd.backlight(); 
  lcd.createChar(1, degree); 
  Serial.begin(9600); 
  dht.begin(); 
  pinMode(flameSensorPin, INPUT); 
  pinMode(PUMP_PIN, OUTPUT); 
} 
 
void loop() { 
  // Измерение датчика датчика DHT11 
  float h = dht.readHumidity(); 
  float t = dht.readTemperature(); 
   
  // Измерение датчика MQ135 
  float ppm = gasSensor.getPPM(); 
   
  // Обнаружение пламени 
  int flame = digitalRead(flameSensorPin); 
   
  // Измерение влажности почвы 
  int soilMoistureValue = analogRead(A0); 
  int percentage = map(soilMoistureValue, 490, 1023, 100, 0); 
   
  // Вывод показаний на LCD дисплей 
  lcd.setCursor(0, 0); 
  lcd.print("Hum = % "); 
  lcd.setCursor(7, 0); 
  lcd.print(h, 1); 
  lcd.setCursor(0, 1); 
  lcd.print("Temp = \1C "); 
  lcd.setCursor(7, 1); 
  lcd.print(t, 1); 
   
  // Вывод показаний на Serial Monitor 
  Serial.print("Humidity: "); 
  Serial.print(h); 
  Serial.print(" %\t"); 
  Serial.print("Temperature: "); 
  Serial.print(t); 
  Serial.println(" °C"); 
  Serial.print("CO2 ppm value: "); 
  Serial.println(ppm); 
  Serial.print("Flame detected: "); 
  Serial.println(flame ? "Yes" : "No"); 
  Serial.print("Soil moisture: "); 
  Serial.print(percentage); 
  Serial.println("%"); 
   
  // Управление насосом в зависимости от влажности почвы 
  if (percentage < 10) { 
    Serial.println("Turning pump on"); 
    digitalWrite(PUMP_PIN, LOW); 
  } 
  if (percentage > 80) { 
    Serial.println("Turning pump off"); 
    digitalWrite(PUMP_PIN, HIGH); 
  } 
   
  delay(2000); 
}
