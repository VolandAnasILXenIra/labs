Красный пин 6
#define R_PIN 6
ЗЕЛЕНЫЙ ПИН 3
#define G_PIN 3
синий пин 5
#define B_PIN 5

void setup( ) {
  	
  	
  	pinMode(R_PIN, OUTPUT);
    pinMode(G_PIN, OUTPUT);
  	pinMode(B_PIN, OUTPUT);
}

void loop() {
  digitalWrite(R_PIN,1);  включает светодиод красным
  delay(1000);  ждет секунду
  digitalWrite(R_PIN,0);  выключает светодиод
  
  digitalWrite(G_PIN,1);  включает светодиод зеленым
  delay(1000);  ждет секунду
  digitalWrite(G_PIN,0);  выключает светодиод
  
  digitalWrite(B_PIN,1);  включает светодиод синим
  delay(1000);  ждет секунду
  digitalWrite(B_PIN,0);  выключает светодиод
}
