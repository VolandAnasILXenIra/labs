#define PUMP_PIN 3 
int soilMoistureValue = 0; 
int percentage=0; 
 
void setup() { 
    pinMode(PUMP_PIN, OUTPUT); 
    Serial.begin(9600); 
} 
 
void loop() { 
SoilMoistureValue = analogRead(A0); 
Serial.println(percentage); 
percentage = map(soilMoistureValue, 490, 1023, 100, 0); 
if(percentage < 10) 
{ 
Serial.println(«pump on»); 
digitalWrite(PUMP_PIN, LOW); 
} 
if(percentage > 80) 
{ 
Serial.println(«pump off»); 
digitalWrite(PUMP_PIN, HIGH); 
} 
}
